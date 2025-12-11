#!/usr/bin/env python
"""
Database Initialization Script for OrganMatch
Run this script once to set up the database with tables and sample data.

Usage:
    python init_db.py

This script will:
1. Create all database tables
2. Create a test user (username: admin, password: admin123)
3. Load sample donor and recipient data
"""

import os
import sys
from app import app, db
from models import User, Donor, Recipient
import pandas as pd

def init_database():
    """Initialize database with tables and sample data"""
    
    with app.app_context():
        print("🔧 Initializing OrganMatch Database...")
        print("=" * 50)
        
        # Create all tables
        print("📋 Creating database tables...")
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Check if admin user exists
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            print("\n👤 Creating test user...")
            admin = User(username='admin', email='admin@organmatch.local')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✅ Test user created!")
            print("   Username: admin")
            print("   Password: admin123")
        else:
            print("\n✅ Admin user already exists")
        
        # Load sample data
        donor_count = Donor.query.count()
        recipient_count = Recipient.query.count()
        
        if donor_count == 0 or recipient_count == 0:
            print("\n📥 Loading sample data...")
            try:
                donors_csv = pd.read_csv('data/donors_sample.csv')
                recipients_csv = pd.read_csv('data/recipients_sample.csv')
                
                for _, row in donors_csv.iterrows():
                    donor = Donor(
                        id=row['id'],
                        name=row['name'],
                        age=row.get('age'),
                        gender=row.get('gender'),
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
                        gender=row.get('gender'),
                        blood_group=row.get('blood_group'),
                        organ_needed=row['organ_needed'],
                        bmi=row.get('bmi'),
                        hla_typing=row.get('hla_typing'),
                        latitude=row.get('latitude'),
                        longitude=row.get('longitude'),
                        organ_size_needed=row.get('organ_size_needed'),
                        diabetes=row.get('diabetes', 0),
                        hypertension=row.get('hypertension', 0),
                        urgency_level=row.get('urgency_level', 5)
                    )
                    db.session.merge(recipient)
                
                db.session.commit()
                print(f"✅ Loaded {len(donors_csv)} donors and {len(recipients_csv)} recipients")
            except FileNotFoundError as e:
                print(f"⚠️  Could not load sample data: {str(e)}")
                print("   Sample data files not found. You can add data manually through the UI.")
        else:
            print(f"\n✅ Database already contains data:")
            print(f"   Donors: {donor_count}")
            print(f"   Recipients: {recipient_count}")
        
        print("\n" + "=" * 50)
        print("✅ Database initialization complete!")
        print("\n📝 Next steps:")
        print("1. Run the application: python app.py")
        print("2. Open http://localhost:5000 in your browser")
        print("3. Login with:")
        print("   Username: admin")
        print("   Password: admin123")
        print("\n💡 You can now add donors and recipients, or use the sample data provided.")

def create_user(username, email, password):
    """Create a new user"""
    with app.app_context():
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print(f"⚠️  User '{username}' already exists")
            return False
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print(f"✅ User '{username}' created successfully!")
        return True

if __name__ == '__main__':
    try:
        import sys
        
        # Check if user wants to create additional users
        if len(sys.argv) > 1 and sys.argv[1] == '--create-user':
            if len(sys.argv) < 5:
                print("Usage: python init_db.py --create-user <username> <email> <password>")
                sys.exit(1)
            
            username = sys.argv[2]
            email = sys.argv[3]
            password = sys.argv[4]
            create_user(username, email, password)
        else:
            init_database()
    except Exception as e:
        print(f"\n❌ Error initializing database: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
