"""
Migration script to move data from SQLite to PostgreSQL
"""
import os
import sys
from app import app, db
from models import User, Donor, Recipient, MatchHistory, SystemLog
from sqlalchemy import create_engine, inspect, func, text
from sqlalchemy.orm import sessionmaker

def migrate_data():
    """Migrate data from SQLite to PostgreSQL"""
    
    # SQLite connection (Flask stores it in instance/ folder)
    sqlite_path = 'instance/organmatch.db'
    sqlite_uri = f'sqlite:///{sqlite_path}'
    sqlite_engine = create_engine(sqlite_uri)
    SqliteSession = sessionmaker(bind=sqlite_engine)
    
    print("🔄 Starting database migration from SQLite to PostgreSQL...")
    
    with app.app_context():
        # Step 1: Create PostgreSQL schema
        print("📊 Creating PostgreSQL schema...")
        db.create_all()
        print("✅ PostgreSQL schema created!")
        
        # Check if SQLite database exists
        if not os.path.exists(sqlite_path):
            print("⚠️  No SQLite database found. Starting with empty PostgreSQL database.")
            print("✅ Migration complete - PostgreSQL is ready to use!")
            return
        
        # Step 2: Check if there's any data in SQLite
        inspector = inspect(sqlite_engine)
        if not inspector.get_table_names():
            print("⚠️  SQLite database is empty. Starting with empty PostgreSQL database.")
            print("✅ Migration complete - PostgreSQL is ready to use!")
            return
        
        # Step 3: Migrate data from SQLite to PostgreSQL
        print("📦 Migrating data from SQLite to PostgreSQL...")
        
        sqlite_session = SqliteSession()
        
        try:
            # Migrate Users (preserve IDs and timestamps)
            users = sqlite_session.query(User).all()
            if users:
                print(f"  → Migrating {len(users)} users...")
                for user in users:
                    new_user = User(
                        id=user.id,
                        username=user.username,
                        email=user.email,
                        password_hash=user.password_hash,
                        created_at=user.created_at
                    )
                    db.session.add(new_user)
                db.session.flush()
                db.session.commit()
                
                # Reset sequence for users table
                max_id = db.session.query(func.max(User.id)).scalar() or 0
                db.session.execute(text(f"SELECT setval('users_id_seq', {max_id})"))
                db.session.commit()
                print(f"  ✅ Migrated {len(users)} users (max ID: {max_id})")
            
            # Migrate Donors (preserve IDs and timestamps)
            donors = sqlite_session.query(Donor).all()
            if donors:
                print(f"  → Migrating {len(donors)} donors...")
                for donor in donors:
                    new_donor = Donor(
                        id=donor.id,
                        name=donor.name,
                        age=donor.age,
                        blood_group=donor.blood_group,
                        organ_type=donor.organ_type,
                        bmi=donor.bmi,
                        hla_typing=donor.hla_typing,
                        latitude=donor.latitude,
                        longitude=donor.longitude,
                        organ_storage_hours=donor.organ_storage_hours,
                        organ_size=donor.organ_size,
                        diabetes=donor.diabetes,
                        hypertension=donor.hypertension,
                        smoking=donor.smoking,
                        alcohol=donor.alcohol,
                        created_at=donor.created_at
                    )
                    db.session.add(new_donor)
                db.session.flush()
                db.session.commit()
                
                # Reset sequence for donors table
                max_id = db.session.query(func.max(Donor.id)).scalar() or 0
                db.session.execute(text(f"SELECT setval('donors_id_seq', {max_id})"))
                db.session.commit()
                print(f"  ✅ Migrated {len(donors)} donors (max ID: {max_id})")
            
            # Migrate Recipients (preserve IDs and timestamps)
            recipients = sqlite_session.query(Recipient).all()
            if recipients:
                print(f"  → Migrating {len(recipients)} recipients...")
                for recipient in recipients:
                    new_recipient = Recipient(
                        id=recipient.id,
                        name=recipient.name,
                        age=recipient.age,
                        blood_group=recipient.blood_group,
                        organ_needed=recipient.organ_needed,
                        bmi=recipient.bmi,
                        hla_typing=recipient.hla_typing,
                        latitude=recipient.latitude,
                        longitude=recipient.longitude,
                        organ_size_needed=recipient.organ_size_needed,
                        diabetes=recipient.diabetes,
                        hypertension=recipient.hypertension,
                        urgency_level=recipient.urgency_level,
                        created_at=recipient.created_at
                    )
                    db.session.add(new_recipient)
                db.session.flush()
                db.session.commit()
                
                # Reset sequence for recipients table
                max_id = db.session.query(func.max(Recipient.id)).scalar() or 0
                db.session.execute(text(f"SELECT setval('recipients_id_seq', {max_id})"))
                db.session.commit()
                print(f"  ✅ Migrated {len(recipients)} recipients (max ID: {max_id})")
            
            # Migrate Match History (preserve IDs and timestamps)
            matches = sqlite_session.query(MatchHistory).all()
            if matches:
                print(f"  → Migrating {len(matches)} match records...")
                for match in matches:
                    new_match = MatchHistory(
                        id=match.id,
                        donor_id=match.donor_id,
                        recipient_id=match.recipient_id,
                        compatibility_score=match.compatibility_score,
                        matched_at=match.matched_at
                    )
                    db.session.add(new_match)
                db.session.flush()
                db.session.commit()
                
                # Reset sequence for match_history table
                max_id = db.session.query(func.max(MatchHistory.id)).scalar() or 0
                db.session.execute(text(f"SELECT setval('match_history_id_seq', {max_id})"))
                db.session.commit()
                print(f"  ✅ Migrated {len(matches)} match records (max ID: {max_id})")
            
            # Migrate System Logs (preserve IDs and timestamps)
            logs = sqlite_session.query(SystemLog).all()
            if logs:
                print(f"  → Migrating {len(logs)} system logs...")
                for log in logs:
                    new_log = SystemLog(
                        id=log.id,
                        message=log.message,
                        level=log.level,
                        category=log.category,
                        timestamp=log.timestamp
                    )
                    db.session.add(new_log)
                db.session.flush()
                db.session.commit()
                
                # Reset sequence for system_logs table
                max_id = db.session.query(func.max(SystemLog.id)).scalar() or 0
                db.session.execute(text(f"SELECT setval('system_logs_id_seq', {max_id})"))
                db.session.commit()
                print(f"  ✅ Migrated {len(logs)} system logs (max ID: {max_id})")
            
            print("\n✅ Migration completed successfully!")
            print("🗄️  Your data is now safely stored in PostgreSQL")
            print("🚀 PostgreSQL database is ready for deployment!")
            
        except Exception as e:
            db.session.rollback()
            print(f"\n❌ Error during migration: {str(e)}")
            sys.exit(1)
        finally:
            sqlite_session.close()

if __name__ == '__main__':
    migrate_data()
