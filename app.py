from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, send_from_directory, session
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from urllib.parse import urlparse
import os
import pandas as pd
from models import db, Donor, Recipient, User, MatchHistory, SystemLog
from ml.train_model import train_model, load_model, get_feature_importance, get_model_metrics, get_model_config, save_model_config
from ml.predict_model import predict_compatibility, get_best_matches
from ml.feature_engineering import (
    calculate_organ_freshness_score, 
    check_blood_compatibility, 
    calculate_hla_match_score,
    calculate_gps_distance,
    calculate_medical_risk_score,
    calculate_gender_compatibility,
    calculate_blood_factor,
    calculate_hla_factor,
    calculate_storage_factor,
    calculate_urgency_factor,
    calculate_medical_risk_factor,
    calculate_age_factor,
    calculate_bmi_factor,
    calculate_size_factor,
    calculate_distance_factor,
    calculate_gender_factor
)
from sqlalchemy import func
import warnings
import threading
import time
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')

database_url = os.environ.get('DATABASE_URL', 'sqlite:///organmatch.db') or 'sqlite:///organmatch.db'
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_recycle': 300,
    'pool_pre_ping': True,
}
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

ALLOWED_EXTENSIONS = {'csv'}

retrain_lock = threading.Lock()
retrain_pending_lock = threading.Lock()
retrain_in_progress = False
retrain_pending = False
retrain_timer = None
retrain_status = {'success': None, 'message': None, 'timestamp': None}

def log_to_db(message, level='info', category='general'):
    """Log messages to database for the Logs page"""
    try:
        with app.app_context():
            log_entry = SystemLog(message=message, level=level, category=category)
            db.session.add(log_entry)
            db.session.commit()
    except:
        pass

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def background_retrain():
    """
    Background task to retrain the model.
    Runs in a separate thread to avoid blocking web requests.
    """
    global retrain_in_progress, retrain_status, retrain_pending, retrain_pending_lock
    
    with app.app_context():
        try:
            print("\n🔄 Auto-retraining model with updated data...")
            log_to_db("🔄 Auto-retraining model with updated data...", 'info', 'training')
            
            donors = Donor.query.all()
            recipients = Recipient.query.all()
            
            if not donors or not recipients:
                print("⚠️ Cannot retrain: Need both donors and recipients in database")
                log_to_db("⚠️ Cannot retrain: Need both donors and recipients in database", 'warning', 'training')
                retrain_status = {
                    'success': False,
                    'message': 'Cannot retrain: Need both donors and recipients in database',
                    'timestamp': time.time()
                }
                return
            
            donors_df = pd.DataFrame([d.to_dict() for d in donors])
            recipients_df = pd.DataFrame([r.to_dict() for r in recipients])
            
            train_model(donors_df, recipients_df)
            
            print("✅ Model retrained successfully with latest data!")
            log_to_db("✅ Model retrained successfully with latest data!", 'success', 'training')
            retrain_status = {
                'success': True,
                'message': 'Model automatically retrained with new data! Matches are now up-to-date.',
                'timestamp': time.time()
            }
            
        except Exception as e:
            print(f"❌ Error during auto-retraining: {str(e)}")
            retrain_status = {
                'success': False,
                'message': f'Model retraining failed: {str(e)}',
                'timestamp': time.time()
            }
        finally:
            retrain_in_progress = False
            
            should_retrain_again = False
            with retrain_pending_lock:
                if retrain_pending:
                    retrain_pending = False
                    should_retrain_again = True
            
            retrain_lock.release()
            
            if should_retrain_again:
                print("🔄 Pending retrain detected, scheduling another round...")
                auto_retrain_model()

def auto_retrain_model():
    """
    Trigger automatic model retraining in the background with debouncing.
    This function returns immediately and doesn't block the web request.
    """
    global retrain_lock, retrain_in_progress, retrain_timer, retrain_pending, retrain_pending_lock
    
    if retrain_in_progress or retrain_lock.locked():
        print("⏳ Retraining already in progress, marking for retry...")
        with retrain_pending_lock:
            retrain_pending = True
        return True
    
    if retrain_timer is not None:
        retrain_timer.cancel()
    
    def start_retrain():
        global retrain_in_progress
        
        if retrain_lock.acquire(blocking=False):
            try:
                retrain_in_progress = True
                thread = threading.Thread(target=background_retrain)
                thread.daemon = True
                thread.start()
            except Exception as e:
                print(f"Failed to start retraining thread: {str(e)}")
                retrain_in_progress = False
                retrain_lock.release()
        else:
            print("⏳ Could not acquire lock, retraining already in progress")
    
    retrain_timer = threading.Timer(3.0, start_retrain)
    retrain_timer.daemon = True
    retrain_timer.start()
    
    return True

def load_sample_data():
    print("📥 Loading sample data into database...")
    
    donors_csv = pd.read_csv('data/donors_sample.csv')
    recipients_csv = pd.read_csv('data/recipients_sample.csv')
    
    for _, row in donors_csv.iterrows():
        donor = Donor(
            id=row['id'],
            name=row['name'],
            age=row.get('age'),
            blood_group=row.get('blood_group'),
            organ_type=row['organ_type'],
            bmi=row.get('bmi'),
            hla_typing=row.get('hla_typing'),
            latitude=row.get('latitude'),
            longitude=row.get('longitude'),
            organ_storage_hours=row.get('organ_storage_hours'),
            organ_size=row.get('organ_size'),
            diabetes=row.get('diabetes', 0),
            hypertension=row.get('hypertension', 0),
            smoking=row.get('smoking', 0),
            alcohol=row.get('alcohol', 0)
        )
        db.session.merge(donor)
    
    for _, row in recipients_csv.iterrows():
        recipient = Recipient(
            id=row['id'],
            name=row['name'],
            age=row.get('age'),
            blood_group=row.get('blood_group'),
            organ_needed=row['organ_needed'],
            bmi=row.get('bmi'),
            hla_typing=row.get('hla_typing'),
            latitude=row.get('latitude'),
            longitude=row.get('longitude'),
            organ_size_needed=row.get('organ_size_needed'),
            diabetes=row.get('diabetes', 0),
            hypertension=row.get('hypertension', 0),
            urgency_level=row.get('urgency_level', 1)
        )
        db.session.merge(recipient)
    
    db.session.commit()
    print(f"✅ Loaded {len(donors_csv)} donors and {len(recipients_csv)} recipients")

def train_initial_model():
    if os.path.exists('models/random_forest.joblib'):
        print("✅ Model already exists, skipping initial training")
        return
    
    print("🎯 Training initial model with sample data...")
    donors = Donor.query.all()
    recipients = Recipient.query.all()
    
    if not donors or not recipients:
        print("⚠️ No data found. Loading sample data first...")
        load_sample_data()
        donors = Donor.query.all()
        recipients = Recipient.query.all()
    
    donors_df = pd.DataFrame([d.to_dict() for d in donors])
    recipients_df = pd.DataFrame([r.to_dict() for r in recipients])
    
    train_model(donors_df, recipients_df)

@app.before_request
def check_retrain_status():
    """
    Check for completed retraining and flash the status to the user.
    This runs before each request to show background task results.
    """
    global retrain_status
    
    if current_user.is_authenticated and not request.path.startswith('/static') and not request.path.startswith('/api'):
        if retrain_status['success'] is not None and retrain_status['timestamp'] is not None:
            if time.time() - retrain_status['timestamp'] < 30:
                if retrain_status['success']:
                    flash(retrain_status['message'], 'info')
                else:
                    flash(retrain_status['message'], 'warning')
                
                retrain_status = {'success': None, 'message': None, 'timestamp': None}

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {username}!', 'success')
            next_page = request.args.get('next')
            if next_page:
                parsed = urlparse(next_page)
                if parsed.scheme or parsed.netloc:
                    next_page = url_for('dashboard')
            else:
                next_page = url_for('dashboard')
            return redirect(next_page)
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not username or not email or not password:
            flash('All fields are required', 'error')
        elif password != confirm_password:
            flash('Passwords do not match', 'error')
        elif User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
        elif User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    donor_count = Donor.query.count()
    recipient_count = Recipient.query.count()
    
    donors = Donor.query.all()
    recipients = Recipient.query.all()
    
    organ_distribution = {}
    for donor in donors:
        organ_distribution[donor.organ_type] = organ_distribution.get(donor.organ_type, 0) + 1
    
    recent_donors = Donor.query.order_by(Donor.created_at.desc()).limit(5).all()
    recent_recipients = Recipient.query.order_by(Recipient.created_at.desc()).limit(5).all()
    
    return render_template('dashboard.html',
                         donor_count=donor_count,
                         recipient_count=recipient_count,
                         organ_distribution=organ_distribution,
                         recent_donors=recent_donors,
                         recent_recipients=recent_recipients)

@app.route('/add_donor', methods=['GET', 'POST'])
@login_required
def add_donor():
    if request.method == 'POST':
        try:
            donor = Donor(
                name=request.form['name'],
                age=int(request.form['age']) if request.form.get('age') else None,
                gender=request.form.get('gender'),
                blood_group=request.form.get('blood_group'),
                organ_type=request.form['organ_type'],
                bmi=float(request.form['bmi']) if request.form.get('bmi') else None,
                hla_typing=request.form.get('hla_typing'),
                latitude=float(request.form['latitude']) if request.form.get('latitude') else None,
                longitude=float(request.form['longitude']) if request.form.get('longitude') else None,
                organ_storage_hours=float(request.form['organ_storage_hours']) if request.form.get('organ_storage_hours') else None,
                organ_size=float(request.form['organ_size']) if request.form.get('organ_size') else None,
                diabetes=int(request.form.get('diabetes', 0)),
                hypertension=int(request.form.get('hypertension', 0)),
                smoking=int(request.form.get('smoking', 0)),
                alcohol=int(request.form.get('alcohol', 0))
            )
            db.session.add(donor)
            db.session.commit()
            
            flash(f'Donor {donor.name} added successfully!', 'success')
            
            auto_retrain_model()
            
            return redirect(url_for('donors'))
        except Exception as e:
            flash(f'Error adding donor: {str(e)}', 'error')
    
    return render_template('add_donor.html')

@app.route('/add_recipient', methods=['GET', 'POST'])
@login_required
def add_recipient():
    if request.method == 'POST':
        try:
            recipient = Recipient(
                name=request.form['name'],
                age=int(request.form['age']) if request.form.get('age') else None,
                gender=request.form.get('gender'),
                blood_group=request.form.get('blood_group'),
                organ_needed=request.form['organ_needed'],
                bmi=float(request.form['bmi']) if request.form.get('bmi') else None,
                hla_typing=request.form.get('hla_typing'),
                latitude=float(request.form['latitude']) if request.form.get('latitude') else None,
                longitude=float(request.form['longitude']) if request.form.get('longitude') else None,
                organ_size_needed=float(request.form['organ_size_needed']) if request.form.get('organ_size_needed') else None,
                diabetes=int(request.form.get('diabetes', 0)),
                hypertension=int(request.form.get('hypertension', 0)),
                urgency_level=int(request.form.get('urgency_level', 1))
            )
            db.session.add(recipient)
            db.session.commit()
            
            flash(f'Recipient {recipient.name} added successfully!', 'success')
            
            auto_retrain_model()
            
            return redirect(url_for('recipients'))
        except Exception as e:
            flash(f'Error adding recipient: {str(e)}', 'error')
    
    return render_template('add_recipient.html')

@app.route('/donors')
@login_required
def donors():
    all_donors = Donor.query.all()
    return render_template('donors.html', donors=all_donors)

@app.route('/donors/export')
@login_required
def export_donors():
    donors = Donor.query.all()
    donors_data = [donor.to_dict() for donor in donors]
    
    donor_columns = ['id', 'name', 'age', 'gender', 'blood_group', 'organ_type', 'bmi', 'hla_typing', 
                     'latitude', 'longitude', 'organ_storage_hours', 'organ_size', 
                     'diabetes', 'hypertension', 'smoking', 'alcohol', 'created_at']
    
    df = pd.DataFrame(donors_data, columns=donor_columns)
    csv_data = df.to_csv(index=False)
    
    from flask import Response
    return Response(
        csv_data,
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename=donors_export.csv'}
    )

@app.route('/recipients')
@login_required
def recipients():
    all_recipients = Recipient.query.all()
    return render_template('recipients.html', recipients=all_recipients)

@app.route('/recipients/export')
@login_required
def export_recipients():
    recipients = Recipient.query.all()
    recipients_data = [recipient.to_dict() for recipient in recipients]
    
    recipient_columns = ['id', 'name', 'age', 'gender', 'blood_group', 'organ_needed', 'bmi', 'hla_typing',
                        'latitude', 'longitude', 'organ_size_needed', 
                        'diabetes', 'hypertension', 'urgency_level', 'created_at']
    
    df = pd.DataFrame(recipients_data, columns=recipient_columns)
    csv_data = df.to_csv(index=False)
    
    from flask import Response
    return Response(
        csv_data,
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename=recipients_export.csv'}
    )

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        donor_file = request.files.get('donor_file')
        recipient_file = request.files.get('recipient_file')
        
        messages = []
        new_donor_ids = []
        new_recipient_ids = []
        
        if donor_file and allowed_file(donor_file.filename):
            try:
                df = pd.read_csv(donor_file)
                count = 0
                donor_objects = []
                for _, row in df.iterrows():
                    donor = Donor(
                        name=row.get('name', 'Unknown'),
                        age=row.get('age'),
                        gender=row.get('gender'),
                        blood_group=row.get('blood_group'),
                        organ_type=row.get('organ_type', 'Unknown'),
                        bmi=row.get('bmi'),
                        hla_typing=row.get('hla_typing'),
                        latitude=row.get('latitude'),
                        longitude=row.get('longitude'),
                        organ_storage_hours=row.get('organ_storage_hours'),
                        organ_size=row.get('organ_size'),
                        diabetes=row.get('diabetes', 0),
                        hypertension=row.get('hypertension', 0),
                        smoking=row.get('smoking', 0),
                        alcohol=row.get('alcohol', 0)
                    )
                    db.session.add(donor)
                    donor_objects.append(donor)
                    count += 1
                db.session.flush()
                for donor in donor_objects:
                    new_donor_ids.append(donor.id)
                db.session.commit()
                messages.append(f'Successfully uploaded {count} donors')
            except Exception as e:
                db.session.rollback()
                messages.append(f'Error uploading donors: {str(e)}')
        
        if recipient_file and allowed_file(recipient_file.filename):
            try:
                df = pd.read_csv(recipient_file)
                count = 0
                recipient_objects = []
                for _, row in df.iterrows():
                    recipient = Recipient(
                        name=row.get('name', 'Unknown'),
                        age=row.get('age'),
                        gender=row.get('gender'),
                        blood_group=row.get('blood_group'),
                        organ_needed=row.get('organ_needed', 'Unknown'),
                        bmi=row.get('bmi'),
                        hla_typing=row.get('hla_typing'),
                        latitude=row.get('latitude'),
                        longitude=row.get('longitude'),
                        organ_size_needed=row.get('organ_size_needed'),
                        diabetes=row.get('diabetes', 0),
                        hypertension=row.get('hypertension', 0),
                        urgency_level=row.get('urgency_level', 1)
                    )
                    db.session.add(recipient)
                    recipient_objects.append(recipient)
                    count += 1
                db.session.flush()
                for recipient in recipient_objects:
                    new_recipient_ids.append(recipient.id)
                db.session.commit()
                messages.append(f'Successfully uploaded {count} recipients')
            except Exception as e:
                db.session.rollback()
                messages.append(f'Error uploading recipients: {str(e)}')
        
        donor_success = False
        recipient_success = False
        
        for msg in messages:
            flash(msg, 'success' if 'Successfully' in msg else 'error')
            if 'Successfully uploaded' in msg and 'donors' in msg:
                donor_success = True
            if 'Successfully uploaded' in msg and 'recipients' in msg:
                recipient_success = True
        
        if donor_success or recipient_success:
            auto_retrain_model()
            
            if donor_success and recipient_success:
                session['uploaded_donor_ids'] = new_donor_ids
                session['uploaded_recipient_ids'] = new_recipient_ids
                return redirect(url_for('upload_summary'))
            elif donor_success:
                return redirect(url_for('donors'))
            else:
                return redirect(url_for('recipients'))
        
        return redirect(url_for('upload'))
    
    return render_template('upload.html')

@app.route('/upload/summary')
@login_required
def upload_summary():
    donor_ids = session.pop('uploaded_donor_ids', [])
    recipient_ids = session.pop('uploaded_recipient_ids', [])
    
    new_donors = Donor.query.filter(Donor.id.in_(donor_ids)).all() if donor_ids else []
    new_recipients = Recipient.query.filter(Recipient.id.in_(recipient_ids)).all() if recipient_ids else []
    
    if not new_donors and not new_recipients:
        flash('No upload data found. Please upload files first.', 'warning')
        return redirect(url_for('upload'))
    
    return render_template('upload_summary.html', donors=new_donors, recipients=new_recipients)

@app.route('/matches')
@login_required
def matches():
    donors = Donor.query.all()
    recipients = Recipient.query.all()
    
    if not donors or not recipients:
        flash('No donors or recipients found. Please add data first.', 'warning')
        return render_template('matches.html', matches=[])
    
    donors_df = pd.DataFrame([d.to_dict() for d in donors])
    recipients_df = pd.DataFrame([r.to_dict() for r in recipients])
    
    predictions = predict_compatibility(donors_df, recipients_df)
    
    matches_with_details = []
    seen_pairs = set()
    
    for pred in predictions:
        donor_id = pred['donor_id']
        recipient_id = pred['recipient_id']
        pair_key = (donor_id, recipient_id)
        
        if pair_key in seen_pairs:
            continue
        
        seen_pairs.add(pair_key)
        
        donor = Donor.query.get(donor_id)
        recipient = Recipient.query.get(recipient_id)
        if donor and recipient:
            compatibility_score = pred['compatibility_percentage']
            
            # Calculate all individual factors
            storage_score = calculate_organ_freshness_score(
                donor.organ_storage_hours,
                donor.organ_type
            )
            
            blood_compatible = check_blood_compatibility(donor.blood_group, recipient.blood_group)
            hla_score = calculate_hla_match_score(donor.hla_typing, recipient.hla_typing)
            hla_percentage = round(hla_score * 100, 1)
            
            distance_km = calculate_gps_distance(
                donor.latitude, donor.longitude,
                recipient.latitude, recipient.longitude
            )
            distance_km = round(distance_km, 1) if not pd.isna(distance_km) else None
            
            age_diff = abs((donor.age or 0) - (recipient.age or 0))
            organ_size_diff = abs((donor.organ_size or 0) - (recipient.organ_size_needed or 0))
            
            donor_medical_risk = calculate_medical_risk_score(
                donor.diabetes, donor.hypertension, donor.smoking, donor.alcohol
            )
            recipient_medical_risk = calculate_medical_risk_score(
                recipient.diabetes, recipient.hypertension, 0, 0
            )
            
            gender_compatibility = calculate_gender_compatibility(
                donor.gender, recipient.gender
            )
            
            # Use centralized factor calculation functions (same as training)
            blood_factor = calculate_blood_factor(blood_compatible)
            hla_factor = calculate_hla_factor(hla_score)
            storage_factor = calculate_storage_factor(storage_score)
            urgency_factor = calculate_urgency_factor(recipient.urgency_level)
            medical_risk_factor = calculate_medical_risk_factor(donor_medical_risk, recipient_medical_risk)
            age_factor = calculate_age_factor(age_diff)
            bmi_factor = calculate_bmi_factor(donor.bmi, recipient.bmi)
            size_factor = calculate_size_factor(organ_size_diff, donor.organ_size)
            distance_factor = calculate_distance_factor(distance_km)
            gender_factor = calculate_gender_factor(donor.gender, recipient.gender)
            
            # Apply all critical factors as multipliers to the ML prediction
            adjusted_compatibility = (compatibility_score * blood_factor * hla_factor * 
                                     storage_factor * medical_risk_factor * age_factor * 
                                     bmi_factor * size_factor * distance_factor * gender_factor * urgency_factor)
            
            # Ensure score stays within 0-100 range
            final_compatibility_score = round(max(0, min(100, adjusted_compatibility)), 2)
            
            matches_with_details.append({
                'donor': donor,
                'recipient': recipient,
                'compatibility': final_compatibility_score,
                'ml_score': round(compatibility_score, 2),
                'factors': {
                    'blood_compatible': blood_compatible,
                    'blood_compatible_text': 'Yes' if blood_compatible else 'No',
                    'hla_percentage': hla_percentage,
                    'storage_score': round(storage_score, 1),
                    'distance_km': distance_km,
                    'age_difference': age_diff,
                    'organ_size_difference': round(organ_size_diff, 1),
                    'donor_bmi': round(donor.bmi, 1) if donor.bmi else 'N/A',
                    'recipient_bmi': round(recipient.bmi, 1) if recipient.bmi else 'N/A',
                    'donor_medical_risk': round(donor_medical_risk * 100, 0),
                    'recipient_medical_risk': round(recipient_medical_risk * 100, 0),
                    'urgency_level': recipient.urgency_level,
                    'gender_compatible': round(gender_compatibility * 100, 0),
                    'blood_factor': round(blood_factor, 2),
                    'hla_factor': round(hla_factor, 2),
                    'storage_factor': round(storage_factor, 2),
                    'medical_risk_factor': round(medical_risk_factor, 2),
                    'age_factor': round(age_factor, 2),
                    'bmi_factor': round(bmi_factor, 2),
                    'size_factor': round(size_factor, 2),
                    'distance_factor': round(distance_factor, 2),
                    'gender_factor': round(gender_factor, 2),
                    'urgency_factor': round(urgency_factor, 2)
                }
            })
            
            if final_compatibility_score >= 50:
                try:
                    existing_match = MatchHistory.query.filter_by(
                        donor_id=donor.id,
                        recipient_id=recipient.id
                    ).first()
                    
                    if not existing_match:
                        match_record = MatchHistory(
                            donor_id=donor.id,
                            recipient_id=recipient.id,
                            compatibility_score=final_compatibility_score
                        )
                        db.session.add(match_record)
                        db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    print(f"Warning: Failed to log match history for D{donor.id}-R{recipient.id}: {str(e)}")
    
    # Sort matches by compatibility percentage in descending order (highest to lowest)
    matches_with_details = sorted(matches_with_details, key=lambda x: x['compatibility'], reverse=True)
    
    return render_template('matches.html', matches=matches_with_details)

@app.route('/evaluate')
@login_required
def evaluate():
    model, feature_columns = load_model()
    config = get_model_config()
    model_exists = model is not None
    
    if not model_exists:
        flash('Model not trained yet. Please train the model first.', 'warning')
        return render_template('evaluate.html', feature_importance={}, metrics=None, config=config, has_sufficient_data=False, model_exists=False)
    
    feature_importance = get_feature_importance(model, feature_columns)
    
    donors = Donor.query.all()
    recipients = Recipient.query.all()
    
    if not donors or not recipients:
        flash('No data available for evaluation. Please add donors and recipients.', 'warning')
        return render_template('evaluate.html', feature_importance=feature_importance, metrics=None, config=config, has_sufficient_data=False, model_exists=True)
    
    donors_df = pd.DataFrame([d.to_dict() for d in donors])
    recipients_df = pd.DataFrame([r.to_dict() for r in recipients])
    
    metrics = get_model_metrics(donors_df, recipients_df)
    
    if metrics is None or metrics.get('n_samples', 0) == 0:
        flash('Unable to generate metrics from current data. Showing model feature importance only.', 'warning')
        return render_template('evaluate.html', feature_importance=feature_importance, metrics=None, config=config, has_sufficient_data=False, model_exists=True)
    
    total_samples = metrics.get('n_samples', 0)
    has_sufficient_data = total_samples >= 5 and metrics.get('confusion_matrix') is not None
    
    if not has_sufficient_data:
        flash('Limited data available (less than 5 samples). Advanced metrics (Confusion Matrix, ROC Curve) are not available.', 'info')
    
    feature_importance = metrics.get('feature_importance', feature_importance)
    
    return render_template('evaluate.html', 
                         feature_importance=feature_importance, 
                         metrics=metrics, 
                         config=config, 
                         has_sufficient_data=has_sufficient_data,
                         model_exists=True)

@app.route('/settings')
@login_required
def settings():
    config = get_model_config()
    return render_template('settings.html', config=config)

@app.route('/api/settings', methods=['POST'])
@login_required
def save_settings():
    try:
        data = request.json
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        try:
            n_estimators = int(data.get('n_estimators', 100))
            max_depth_raw = data.get('max_depth')
            
            if max_depth_raw is None or max_depth_raw == '' or max_depth_raw == 0:
                max_depth = None
            else:
                max_depth = int(max_depth_raw)
            
            min_samples_split = int(data.get('min_samples_split', 5))
            min_samples_leaf = int(data.get('min_samples_leaf', 2))
        except (ValueError, TypeError) as e:
            return jsonify({'error': f'Invalid parameter values: {str(e)}'}), 400
        
        if n_estimators < 10 or n_estimators > 500:
            return jsonify({'error': 'n_estimators must be between 10 and 500'}), 400
        if max_depth is not None and (max_depth < 3 or max_depth > 50):
            return jsonify({'error': 'max_depth must be between 3 and 50 (or None for unlimited)'}), 400
        if min_samples_split < 2 or min_samples_split > 20:
            return jsonify({'error': 'min_samples_split must be between 2 and 20'}), 400
        if min_samples_leaf < 1 or min_samples_leaf > 20:
            return jsonify({'error': 'min_samples_leaf must be between 1 and 20'}), 400
        
        config = {
            'n_estimators': n_estimators,
            'max_depth': max_depth,
            'min_samples_split': min_samples_split,
            'min_samples_leaf': min_samples_leaf
        }
        
        save_model_config(config)
        
        donors = Donor.query.all()
        recipients = Recipient.query.all()
        
        if donors and recipients:
            donors_df = pd.DataFrame([d.to_dict() for d in donors])
            recipients_df = pd.DataFrame([r.to_dict() for r in recipients])
            train_model(donors_df, recipients_df, custom_params=config)
            message = 'Settings saved and model retrained successfully!'
        else:
            message = 'Settings saved! Model will be trained when data is available.'
        
        return jsonify({'message': message}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/retrain', methods=['POST'])
def retrain():
    try:
        donors = Donor.query.all()
        recipients = Recipient.query.all()
        
        if not donors or not recipients:
            return jsonify({'error': 'No data available for training'}), 400
        
        donors_df = pd.DataFrame([d.to_dict() for d in donors])
        recipients_df = pd.DataFrame([r.to_dict() for r in recipients])
        
        train_model(donors_df, recipients_df)
        
        return jsonify({'message': 'Model retrained successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.json
        donor_id = data.get('donor_id')
        recipient_id = data.get('recipient_id')
        
        donor = Donor.query.get(donor_id)
        recipient = Recipient.query.get(recipient_id)
        
        if not donor or not recipient:
            return jsonify({'error': 'Donor or recipient not found'}), 404
        
        donors_df = pd.DataFrame([donor.to_dict()])
        recipients_df = pd.DataFrame([recipient.to_dict()])
        
        predictions = predict_compatibility(donors_df, recipients_df)
        
        if predictions:
            return jsonify(predictions[0]), 200
        else:
            return jsonify({'error': 'No prediction available'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/update_donor_location/<int:donor_id>', methods=['POST'])
@login_required
def update_donor_location(donor_id):
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
        
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        if latitude is None or longitude is None:
            return jsonify({'error': 'Latitude and longitude are required'}), 400
        
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except (ValueError, TypeError):
            return jsonify({'error': 'Latitude and longitude must be valid numbers'}), 400
        
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            return jsonify({'error': 'Invalid coordinate values'}), 400
        
        donor = Donor.query.get(donor_id)
        if not donor:
            return jsonify({'error': 'Donor not found'}), 404
        
        donor.latitude = latitude
        donor.longitude = longitude
        db.session.commit()
        
        return jsonify({
            'message': 'Location updated successfully',
            'latitude': donor.latitude,
            'longitude': donor.longitude
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/update_recipient_location/<int:recipient_id>', methods=['POST'])
@login_required
def update_recipient_location(recipient_id):
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
        
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        if latitude is None or longitude is None:
            return jsonify({'error': 'Latitude and longitude are required'}), 400
        
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except (ValueError, TypeError):
            return jsonify({'error': 'Latitude and longitude must be valid numbers'}), 400
        
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            return jsonify({'error': 'Invalid coordinate values'}), 400
        
        recipient = Recipient.query.get(recipient_id)
        if not recipient:
            return jsonify({'error': 'Recipient not found'}), 404
        
        recipient.latitude = latitude
        recipient.longitude = longitude
        db.session.commit()
        
        return jsonify({
            'message': 'Location updated successfully',
            'latitude': recipient.latitude,
            'longitude': recipient.longitude
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/distances')
@login_required
def distances():
    from geopy.distance import geodesic
    
    donors = Donor.query.all()
    recipients = Recipient.query.all()
    
    distances_data = []
    
    for donor in donors:
        if donor.latitude is not None and donor.longitude is not None:
            for recipient in recipients:
                if recipient.latitude is not None and recipient.longitude is not None:
                    donor_coords = (donor.latitude, donor.longitude)
                    recipient_coords = (recipient.latitude, recipient.longitude)
                    distance_km = geodesic(donor_coords, recipient_coords).kilometers
                    
                    distances_data.append({
                        'donor': donor,
                        'recipient': recipient,
                        'distance_km': round(distance_km, 2)
                    })
    
    distances_data.sort(key=lambda x: x['distance_km'])
    
    return render_template('distances.html', distances=distances_data)

@app.route('/api/monthly', methods=['GET'])
@login_required
def api_monthly():
    """Return monthly match statistics for dashboard charts"""
    try:
        monthly_stats = db.session.query(
            func.strftime('%Y-%m', MatchHistory.matched_at).label('month'),
            func.count(MatchHistory.id).label('count'),
            func.avg(MatchHistory.compatibility_score).label('avg_compatibility')
        ).group_by('month').order_by('month').all()
        
        months = []
        counts = []
        avg_scores = []
        
        for stat in monthly_stats:
            months.append(stat.month)
            counts.append(stat.count)
            avg_scores.append(round(stat.avg_compatibility, 2) if stat.avg_compatibility else 0)
        
        if not months:
            from datetime import datetime, timedelta
            today = datetime.now()
            for i in range(5, -1, -1):
                month_date = today - timedelta(days=i*30)
                months.append(month_date.strftime('%Y-%m'))
                counts.append(0)
                avg_scores.append(0)
        
        return jsonify({
            'months': months,
            'match_counts': counts,
            'average_compatibility': avg_scores
        }), 200
    except Exception as e:
        return jsonify({
            'months': [],
            'match_counts': [],
            'average_compatibility': [],
            'error': str(e)
        }), 500

@app.route('/api/evaluate', methods=['GET'])
@login_required
def api_evaluate():
    """Return comprehensive model evaluation metrics"""
    try:
        donors = Donor.query.all()
        recipients = Recipient.query.all()
        
        if not donors or not recipients:
            return jsonify({'error': 'No data available'}), 400
        
        donors_df = pd.DataFrame([d.to_dict() for d in donors])
        recipients_df = pd.DataFrame([r.to_dict() for r in recipients])
        
        metrics = get_model_metrics(donors_df, recipients_df)
        
        if metrics is None:
            return jsonify({'error': 'Could not evaluate model'}), 500
        
        return jsonify(metrics), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/data/<path:filename>')
def serve_data_file(filename):
    return send_from_directory('data', filename)

@app.route('/logs')
@login_required
def logs():
    page = request.args.get('page', 1, type=int)
    per_page = 100
    
    logs_query = SystemLog.query.order_by(SystemLog.timestamp.asc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('logs.html', logs=logs_query)

@app.route('/api/logs')
@login_required
def api_logs():
    limit = request.args.get('limit', 50, type=int)
    category = request.args.get('category', None)
    
    query = SystemLog.query
    if category:
        query = query.filter_by(category=category)
    
    logs = query.order_by(SystemLog.timestamp.asc()).limit(limit).all()
    return jsonify([log.to_dict() for log in logs]), 200

@app.route('/api/logs/clear', methods=['POST'])
@login_required
def clear_logs():
    try:
        SystemLog.query.delete()
        db.session.commit()
        return jsonify({'message': 'Logs cleared successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        if Donor.query.count() == 0:
            load_sample_data()
        
        train_initial_model()
    
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
