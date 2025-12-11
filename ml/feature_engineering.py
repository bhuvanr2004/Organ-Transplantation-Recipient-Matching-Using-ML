import numpy as np
import pandas as pd
from geopy.distance import geodesic
import warnings
warnings.filterwarnings('ignore')

def calculate_hla_match_score(donor_hla, recipient_hla):
    if pd.isna(donor_hla) or pd.isna(recipient_hla):
        return 0.5
    
    if not donor_hla or not recipient_hla:
        return 0.5
    
    donor_alleles = str(donor_hla).upper().replace(' ', '').split(',')
    recipient_alleles = str(recipient_hla).upper().replace(' ', '').split(',')
    
    if len(donor_alleles) == 0 or len(recipient_alleles) == 0:
        return 0.5
    
    matches = sum(1 for allele in donor_alleles if allele in recipient_alleles)
    total = max(len(donor_alleles), len(recipient_alleles))
    
    return matches / total if total > 0 else 0.5

def check_blood_compatibility(donor_bg, recipient_bg):
    if pd.isna(donor_bg) or pd.isna(recipient_bg):
        return 0
    
    compatibility_matrix = {
        'O+': ['O+', 'A+', 'B+', 'AB+'],
        'O-': ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-'],
        'A+': ['A+', 'AB+'],
        'A-': ['A+', 'A-', 'AB+', 'AB-'],
        'B+': ['B+', 'AB+'],
        'B-': ['B+', 'B-', 'AB+', 'AB-'],
        'AB+': ['AB+'],
        'AB-': ['AB+', 'AB-']
    }
    
    donor_bg = str(donor_bg).strip().upper()
    recipient_bg = str(recipient_bg).strip().upper()
    
    if donor_bg not in compatibility_matrix:
        return 0
    
    return 1 if recipient_bg in compatibility_matrix.get(donor_bg, []) else 0

def calculate_gps_distance(donor_lat, donor_lon, recipient_lat, recipient_lon):
    if pd.isna(donor_lat) or pd.isna(donor_lon) or pd.isna(recipient_lat) or pd.isna(recipient_lon):
        return np.nan
    
    try:
        donor_coords = (float(donor_lat), float(donor_lon))
        recipient_coords = (float(recipient_lat), float(recipient_lon))
        return geodesic(donor_coords, recipient_coords).kilometers
    except:
        return np.nan

def calculate_organ_freshness_score(storage_hours, organ_type):
    max_storage_times = {
        'Kidney': 36,
        'Liver': 12,
        'Heart': 6,
        'Lung': 8,
        'Intestine': 6
    }
    
    if pd.isna(storage_hours):
        return 0
    
    if not organ_type or str(organ_type).strip() == '':
        return 0
    
    organ_type_normalized = str(organ_type).strip().capitalize()
    
    if organ_type_normalized not in max_storage_times:
        return 0
    
    storage_hours = float(storage_hours)
    max_hours = max_storage_times[organ_type_normalized]
    
    score = (1 - storage_hours / max_hours) * 100
    
    return max(0, min(100, score))

def calculate_medical_risk_score(diabetes, hypertension, smoking, alcohol):
    risk = 0
    if not pd.isna(diabetes) and diabetes == 1:
        risk += 0.25
    if not pd.isna(hypertension) and hypertension == 1:
        risk += 0.25
    if not pd.isna(smoking) and smoking == 1:
        risk += 0.25
    if not pd.isna(alcohol) and alcohol == 1:
        risk += 0.25
    return risk

def calculate_gender_compatibility(donor_gender, recipient_gender):
    if pd.isna(donor_gender) or pd.isna(recipient_gender):
        return 0.7
    
    if not donor_gender or not recipient_gender or str(donor_gender).strip() == '' or str(recipient_gender).strip() == '':
        return 0.7
    
    donor_gender_normalized = str(donor_gender).strip().lower()
    recipient_gender_normalized = str(recipient_gender).strip().lower()
    
    if donor_gender_normalized == recipient_gender_normalized:
        return 0.8
    else:
        return 0.6

def log_to_db_if_available(message, level='warning', category='training'):
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

def calculate_blood_factor(blood_compatible):
    """Blood incompatibility is a major factor - significantly reduce score"""
    return 1.0 if blood_compatible else 0.15

def calculate_hla_factor(hla_score):
    """HLA match: convert percentage to multiplier (0.3 to 1.0 range)"""
    hla_percentage = hla_score * 100
    return max(0.3, hla_percentage / 100.0)

def calculate_storage_factor(storage_score):
    """Storage score: convert percentage to multiplier (0.4 to 1.0 range)"""
    return max(0.4, storage_score / 100.0)

def calculate_urgency_factor(urgency_level):
    """Urgency affects weighting (higher urgency = willing to accept slight risk)"""
    urgency = float(urgency_level) if urgency_level else 1
    return min(1.15, 0.8 + (urgency / 10.0) * 0.35)

def calculate_medical_risk_factor(donor_medical_risk, recipient_medical_risk):
    """Medical Risk Assessment - penalize high-risk donors or recipients"""
    combined_medical_risk = (donor_medical_risk + recipient_medical_risk) / 2
    return max(0.4, 1.0 - (combined_medical_risk * 0.6))

def calculate_age_factor(age_diff):
    """Age Compatibility - penalize large age differences (ideal: within 20 years)"""
    return 1.0 if age_diff <= 5 else max(0.5, 1.0 - (age_diff - 5) * 0.015)

def calculate_bmi_factor(donor_bmi, recipient_bmi):
    """BMI Compatibility - penalize significant BMI mismatches"""
    donor_bmi_val = donor_bmi if donor_bmi else 25
    recipient_bmi_val = recipient_bmi if recipient_bmi else 25
    bmi_difference = abs(donor_bmi_val - recipient_bmi_val)
    return max(0.6, 1.0 - (bmi_difference * 0.025))

def calculate_size_factor(organ_size_diff, donor_organ_size):
    """Organ Size Compatibility - penalize significant size mismatches"""
    size_difference_pct = (organ_size_diff / max(donor_organ_size or 1, 0.1)) * 100 if donor_organ_size else 0
    return max(0.5, 1.0 - (min(size_difference_pct, 30) * 0.015))

def calculate_distance_factor(distance_km):
    """Distance Factor - penalize long distances (affects organ viability transit time)"""
    if pd.isna(distance_km) or distance_km is None:
        return 0.9  # Unknown distance = slight penalty
    if distance_km <= 500:
        return 1.0
    elif distance_km <= 1000:
        return 0.85
    elif distance_km <= 2000:
        return 0.6
    else:
        return 0.4

def calculate_gender_factor(donor_gender, recipient_gender):
    """Gender Compatibility - minor bonus for same gender"""
    if pd.isna(donor_gender) or pd.isna(recipient_gender):
        return 1.0
    if not donor_gender or not recipient_gender:
        return 1.0
    donor_g = str(donor_gender).strip().lower()
    recipient_g = str(recipient_gender).strip().lower()
    return 1.05 if donor_g == recipient_g else 1.0


def create_features(donors_df, recipients_df):
    features = []
    labels = []
    
    for _, recipient in recipients_df.iterrows():
        for _, donor in donors_df.iterrows():
            if donor['organ_type'] != recipient['organ_needed']:
                continue
            
            feature_dict = {}
            
            # Base features
            feature_dict['hla_match_score'] = calculate_hla_match_score(
                donor.get('hla_typing'), 
                recipient.get('hla_typing')
            )
            
            feature_dict['blood_group_compatible'] = check_blood_compatibility(
                donor.get('blood_group'), 
                recipient.get('blood_group')
            )
            
            feature_dict['organ_freshness_score'] = calculate_organ_freshness_score(
                donor.get('organ_storage_hours'),
                donor['organ_type']
            )
            
            feature_dict['gps_distance_km'] = calculate_gps_distance(
                donor.get('latitude'), donor.get('longitude'),
                recipient.get('latitude'), recipient.get('longitude')
            )
            
            feature_dict['age_difference'] = abs(
                float(donor.get('age', 0) or 0) - float(recipient.get('age', 0) or 0)
            )
            
            feature_dict['organ_size_difference'] = abs(
                float(donor.get('organ_size', 0) or 0) - float(recipient.get('organ_size_needed', 0) or 0)
            )
            
            donor_bmi_value = donor.get('bmi')
            if pd.isna(donor_bmi_value) or donor_bmi_value == 0 or donor_bmi_value == '':
                msg = f"⚠ Missing BMI value for donor {donor['id']} — using average."
                print(msg)
                log_to_db_if_available(msg)
                feature_dict['donor_bmi'] = 0
            else:
                feature_dict['donor_bmi'] = float(donor_bmi_value)
            
            recipient_bmi_value = recipient.get('bmi')
            if pd.isna(recipient_bmi_value) or recipient_bmi_value == 0 or recipient_bmi_value == '':
                msg = f"⚠ Missing BMI value for recipient {recipient['id']} — using average."
                print(msg)
                log_to_db_if_available(msg)
                feature_dict['recipient_bmi'] = 0
            else:
                feature_dict['recipient_bmi'] = float(recipient_bmi_value)
            
            feature_dict['donor_medical_risk'] = calculate_medical_risk_score(
                donor.get('diabetes'), donor.get('hypertension'),
                donor.get('smoking'), donor.get('alcohol')
            )
            
            feature_dict['recipient_medical_risk'] = calculate_medical_risk_score(
                recipient.get('diabetes'), recipient.get('hypertension'),
                0, 0
            )
            
            feature_dict['urgency_level'] = float(recipient.get('urgency_level', 1) or 1)
            
            feature_dict['gender_compatible'] = calculate_gender_compatibility(
                donor.get('gender'),
                recipient.get('gender')
            )
            
            # NEW: Derived factor features (matching matches route logic)
            feature_dict['blood_factor'] = calculate_blood_factor(feature_dict['blood_group_compatible'])
            feature_dict['hla_factor'] = calculate_hla_factor(feature_dict['hla_match_score'])
            feature_dict['storage_factor'] = calculate_storage_factor(feature_dict['organ_freshness_score'])
            feature_dict['urgency_factor'] = calculate_urgency_factor(feature_dict['urgency_level'])
            feature_dict['medical_risk_factor'] = calculate_medical_risk_factor(
                feature_dict['donor_medical_risk'], 
                feature_dict['recipient_medical_risk']
            )
            feature_dict['age_factor'] = calculate_age_factor(feature_dict['age_difference'])
            feature_dict['bmi_factor'] = calculate_bmi_factor(
                feature_dict['donor_bmi'], 
                feature_dict['recipient_bmi']
            )
            feature_dict['size_factor'] = calculate_size_factor(
                feature_dict['organ_size_difference'],
                float(donor.get('organ_size', 0) or 0)
            )
            feature_dict['distance_factor'] = calculate_distance_factor(feature_dict['gps_distance_km'])
            feature_dict['gender_factor'] = calculate_gender_factor(
                donor.get('gender'),
                recipient.get('gender')
            )
            
            # Combined factor score (product of all factors)
            feature_dict['combined_factor_score'] = (
                feature_dict['blood_factor'] * 
                feature_dict['hla_factor'] * 
                feature_dict['storage_factor'] * 
                feature_dict['medical_risk_factor'] * 
                feature_dict['age_factor'] * 
                feature_dict['bmi_factor'] * 
                feature_dict['size_factor'] * 
                feature_dict['distance_factor'] * 
                feature_dict['gender_factor'] * 
                feature_dict['urgency_factor']
            )
            
            feature_dict['donor_id'] = donor['id']
            feature_dict['recipient_id'] = recipient['id']
            
            features.append(feature_dict)
            
            # Enhanced label calculation using all factors
            compatibility_score = (
                feature_dict['hla_match_score'] * 0.25 +
                feature_dict['blood_group_compatible'] * 0.25 +
                (feature_dict['organ_freshness_score'] / 100) * 0.15 +
                (1 - min(feature_dict['donor_medical_risk'], 1)) * 0.1 +
                (1 - min(feature_dict['recipient_medical_risk'], 1)) * 0.1 +
                feature_dict['combined_factor_score'] * 0.15
            )
            
            label = 1 if compatibility_score > 0.5 else 0
            labels.append(label)
    
    return pd.DataFrame(features), labels
