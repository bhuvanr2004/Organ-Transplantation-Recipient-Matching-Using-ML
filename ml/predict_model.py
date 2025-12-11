import pandas as pd
import numpy as np
from ml.feature_engineering import create_features
from ml.train_model import load_model
import warnings
warnings.filterwarnings('ignore')

def predict_compatibility(donors_df, recipients_df, model_path='models/random_forest.joblib'):
    model, feature_columns = load_model(model_path)
    
    if model is None:
        print("⚠️ Model not loaded. Please train the model first.")
        return []
    
    print("🔮 Predicting compatibility for all donor-recipient pairs...")
    
    X_df, _ = create_features(donors_df, recipients_df)
    
    if len(X_df) == 0:
        print("⚠️ No valid donor-recipient pairs to predict.")
        return []
    
    X = X_df[feature_columns].copy()
    for col in X.columns:
        median_value = X[col].median()
        if pd.isna(median_value):
            X[col] = X[col].fillna(0)
            print(f"⚠️ Column '{col}' has no values during prediction - using 0 as default")
        else:
            X[col] = X[col].fillna(median_value)
    
    predictions_proba = model.predict_proba(X)[:, 1]
    
    compatibility_percentage = predictions_proba * 100
    
    results = []
    for i, row in X_df.iterrows():
        results.append({
            'donor_id': int(row['donor_id']),
            'recipient_id': int(row['recipient_id']),
            'compatibility_percentage': round(float(compatibility_percentage[i]), 2)
        })
    
    results.sort(key=lambda x: x['compatibility_percentage'], reverse=True)
    
    print(f"✅ Predicted compatibility for {len(results)} donor-recipient pairs")
    
    return results

def get_best_matches(recipient_id, donors_df, recipients_df, top_n=5, model_path='models/random_forest.joblib'):
    recipient_df = recipients_df[recipients_df['id'] == recipient_id]
    
    if recipient_df.empty:
        return []
    
    all_predictions = predict_compatibility(donors_df, recipient_df, model_path)
    
    top_matches = sorted(all_predictions, key=lambda x: x['compatibility_percentage'], reverse=True)[:top_n]
    
    return top_matches
