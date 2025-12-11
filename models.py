from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Donor(db.Model):
    __tablename__ = 'donors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    blood_group = db.Column(db.String(5), nullable=True)
    organ_type = db.Column(db.String(50), nullable=False)
    bmi = db.Column(db.Float, nullable=True)
    hla_typing = db.Column(db.String(200), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    organ_storage_hours = db.Column(db.Float, nullable=True)
    organ_size = db.Column(db.Float, nullable=True)
    diabetes = db.Column(db.Integer, default=0)
    hypertension = db.Column(db.Integer, default=0)
    smoking = db.Column(db.Integer, default=0)
    alcohol = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'blood_group': self.blood_group,
            'organ_type': self.organ_type,
            'bmi': self.bmi,
            'hla_typing': self.hla_typing,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'organ_storage_hours': self.organ_storage_hours,
            'organ_size': self.organ_size,
            'diabetes': self.diabetes,
            'hypertension': self.hypertension,
            'smoking': self.smoking,
            'alcohol': self.alcohol,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class Recipient(db.Model):
    __tablename__ = 'recipients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    blood_group = db.Column(db.String(5), nullable=True)
    organ_needed = db.Column(db.String(50), nullable=False)
    bmi = db.Column(db.Float, nullable=True)
    hla_typing = db.Column(db.String(200), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    organ_size_needed = db.Column(db.Float, nullable=True)
    diabetes = db.Column(db.Integer, default=0)
    hypertension = db.Column(db.Integer, default=0)
    urgency_level = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'blood_group': self.blood_group,
            'organ_needed': self.organ_needed,
            'bmi': self.bmi,
            'hla_typing': self.hla_typing,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'organ_size_needed': self.organ_size_needed,
            'diabetes': self.diabetes,
            'hypertension': self.hypertension,
            'urgency_level': self.urgency_level,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class MatchHistory(db.Model):
    __tablename__ = 'match_history'
    
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('donors.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('recipients.id'), nullable=False)
    compatibility_score = db.Column(db.Float, nullable=False)
    matched_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    donor = db.relationship('Donor', backref='matches')
    recipient = db.relationship('Recipient', backref='matches')
    
    def to_dict(self):
        return {
            'id': self.id,
            'donor_id': self.donor_id,
            'recipient_id': self.recipient_id,
            'compatibility_score': self.compatibility_score,
            'matched_at': self.matched_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class SystemLog(db.Model):
    __tablename__ = 'system_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    level = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), default='general')
    
    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'level': self.level,
            'message': self.message,
            'category': self.category
        }
