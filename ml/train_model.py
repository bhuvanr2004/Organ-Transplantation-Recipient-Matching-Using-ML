import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import joblib
import os
import json
import warnings
from ml.feature_engineering import create_features
warnings.filterwarnings('ignore')

def log_to_db_if_available(message, level='info', category='training'):
    """Try to log to database if Flask app context is available"""
    try:
        from flask import current_app
        if current_app:
            from models import db, SystemLog
            log_entry = SystemLog(message=message, level=level, category=category)
            db.session.add(log_entry)
            db.session.commit()
    except:
        pass

def get_model_config(config_path='models/model_config.json'):
    default_config = {
        'n_estimators': 100,
        'max_depth': 10,
        'min_samples_split': 5,
        'min_samples_leaf': 2
    }
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                result = default_config.copy()
                for key, value in config.items():
                    if key in result:
                        result[key] = value
                return result
        except:
            pass
    
    return default_config

def save_model_config(config, config_path='models/model_config.json'):
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    
    existing_config = {}
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                existing_config = json.load(f)
        except:
            pass
    
    merged_config = {**existing_config, **config}
    
    with open(config_path, 'w') as f:
        json.dump(merged_config, f, indent=2)

def train_model(donors_df, recipients_df, model_path='models/random_forest.joblib', custom_params=None):
    print("🔧 Creating features from donor-recipient pairs...")
    log_to_db_if_available("🔧 Creating features from donor-recipient pairs...")
    
    X_df, y = create_features(donors_df, recipients_df)
    
    if len(X_df) == 0:
        msg = "⚠️ No valid donor-recipient pairs found. Cannot train model."
        print(msg)
        log_to_db_if_available(msg, 'warning')
        return None
    
    if len(X_df) < 5:
        print(f"⚠️ Only {len(X_df)} samples available. Need at least 5 for proper training.")
        print("   Using all data for training (no test split).")
    
    feature_columns = [col for col in X_df.columns if col not in ['donor_id', 'recipient_id']]
    
    X = X_df[feature_columns].copy()
    for col in X.columns:
        median_value = X[col].median()
        if pd.isna(median_value):
            X[col] = X[col].fillna(0)
            print(f"⚠️ Column '{col}' has no values - using 0 as default")
        else:
            X[col] = X[col].fillna(median_value)
    
    if len(X_df) >= 5:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    else:
        X_train, X_test, y_train, y_test = X, X[:0], y, y[:0]
    
    print(f"📊 Training on {len(X_train)} samples, testing on {len(X_test)} samples...")
    
    if custom_params is None:
        custom_params = get_model_config()
    
    print(f"🔧 Model Parameters: {custom_params}")
    
    max_depth_val = custom_params.get('max_depth', 10)
    
    model = RandomForestClassifier(
        n_estimators=custom_params.get('n_estimators', 100),
        max_depth=max_depth_val if max_depth_val is not None else None,
        min_samples_split=custom_params.get('min_samples_split', 5),
        min_samples_leaf=custom_params.get('min_samples_leaf', 2),
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    
    msg = "✅ Model trained successfully!"
    print(f"\n{msg}")
    log_to_db_if_available(msg, 'success')
    
    if len(X_test) > 0:
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        print("\n📈 Classification Report:")
        print(classification_report(y_test, y_pred, zero_division=0))
        
        try:
            auc_score = roc_auc_score(y_test, y_pred_proba)
            print(f"\n🎯 ROC AUC Score: {auc_score:.4f}")
        except:
            print("\n⚠️ Could not calculate ROC AUC (may need more diverse data)")
        
        print("\n🔢 Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
    else:
        print("\n⚠️ Skipping evaluation metrics (insufficient test data)")
    
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump({
        'model': model,
        'feature_columns': feature_columns,
        'model_params': custom_params
    }, model_path)
    
    save_model_config(custom_params)
    
    msg = f"💾 Model saved to {model_path}"
    print(f"\n{msg}")
    log_to_db_if_available(msg, 'success')
    
    return model

def load_model(model_path='models/random_forest.joblib'):
    if not os.path.exists(model_path):
        print(f"⚠️ Model not found at {model_path}")
        return None, None
    
    print(f"📥 Loading model from {model_path}...")
    model_data = joblib.load(model_path)
    return model_data['model'], model_data['feature_columns']

def get_feature_importance(model, feature_columns):
    if model is None:
        return {}
    
    importances = model.feature_importances_
    feature_importance_dict = dict(zip(feature_columns, importances))
    return dict(sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True))

def get_model_metrics(donors_df, recipients_df, model_path='models/random_forest.joblib'):
    """Get comprehensive model evaluation metrics including ROC and confusion matrix"""
    model, feature_columns = load_model(model_path)
    if model is None:
        return None
    
    X_df, y = create_features(donors_df, recipients_df)
    if len(X_df) == 0:
        return None
    
    X = X_df[feature_columns].copy()
    for col in X.columns:
        median_value = X[col].median()
        X[col] = X[col].fillna(median_value if not pd.isna(median_value) else 0)
    
    metrics = {
        'feature_importance': get_feature_importance(model, feature_columns),
        'n_samples': len(X),
        'n_features': len(feature_columns),
        'confusion_matrix': None,
        'classification_report': None,
        'roc_curve': None
    }
    
    if len(X_df) < 5:
        return metrics
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    if len(X_test) > 0:
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        metrics['confusion_matrix'] = confusion_matrix(y_test, y_pred).tolist()
        metrics['classification_report'] = classification_report(y_test, y_pred, zero_division=0, output_dict=True)
        
        try:
            fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
            metrics['roc_curve'] = {
                'fpr': fpr.tolist(),
                'tpr': tpr.tolist(),
                'auc_score': roc_auc_score(y_test, y_pred_proba)
            }
        except:
            metrics['roc_curve'] = None
    
    return metrics
