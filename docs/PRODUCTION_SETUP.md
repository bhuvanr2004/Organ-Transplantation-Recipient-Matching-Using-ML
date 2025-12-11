# Production Deployment Guide for OrganMatch

## ⚠️ Important Security Notes

The default setup is configured for **development only**. Before deploying to production, you MUST complete the following steps:

---

## 1. Environment Variables

Create a `.env` file or set these environment variables:

```bash
# Required for Production
SESSION_SECRET=your-strong-random-secret-key-here-min-32-chars
FLASK_DEBUG=false

# Optional (defaults shown)
DATABASE_URL=sqlite:///organmatch.db
```

### Generate a secure SECRET_KEY:

```python
import secrets
print(secrets.token_hex(32))
```

Or using command line:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## 2. Production WSGI Server

**DO NOT use Flask's built-in server in production!**

### Option A: Gunicorn (Recommended)

Install:
```bash
pip install gunicorn
```

Run:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 --reuse-port app:app
```

### Option B: uWSGI

Install:
```bash
pip install uwsgi
```

Run:
```bash
uwsgi --http 0.0.0.0:5000 --wsgi-file app.py --callable app --processes 4
```

---

## 3. Database Migration

For production, consider using **PostgreSQL** instead of SQLite:

### Install PostgreSQL dependencies:
```bash
pip install psycopg2-binary
```

### Update database URL:
```python
# In app.py or via environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/organmatch'
```

---

## 4. Security Hardening

### A. Disable Debug Mode
Already handled if `FLASK_DEBUG=false` is set in environment.

### B. Set Secure Session Cookie Flags
Add to `app.py`:
```python
app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
```

### C. Enable HTTPS
Use a reverse proxy (nginx, Apache) with SSL certificates:

**Nginx example config:**
```nginx
server {
    listen 443 ssl;
    server_name organmatch.example.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### D. Rate Limiting
Consider adding Flask-Limiter:
```bash
pip install Flask-Limiter
```

```python
from flask_limiter import Limiter
limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/retrain', methods=['POST'])
@limiter.limit("5 per hour")
def retrain():
    # ...
```

---

## 5. File Upload Security

Already implemented:
- ✅ File type validation (CSV only)
- ✅ Secure filename sanitization
- ✅ Max file size limit (16MB)

For additional security:
- Store uploads outside the web root
- Scan uploaded files for malware
- Use dedicated storage service (S3, etc.)

---

## 6. Monitoring and Logging

### Setup Application Logging:
```python
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('organmatch.log', maxBytes=10000000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
```

### Monitor ML Model Performance:
- Track prediction accuracy over time
- Log retrain operations
- Alert on model degradation

---

## 7. Backup Strategy

### Database Backups:
```bash
# SQLite
cp organmatch.db organmatch_backup_$(date +%Y%m%d).db

# PostgreSQL
pg_dump organmatch > organmatch_backup_$(date +%Y%m%d).sql
```

### Model Backups:
```bash
cp models/random_forest.joblib models/random_forest_backup_$(date +%Y%m%d).joblib
```

### Automated Backup Script:
```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p backups/$DATE
cp organmatch.db backups/$DATE/
cp models/random_forest.joblib backups/$DATE/
find backups/* -mtime +30 -delete  # Keep last 30 days
```

---

## 8. Performance Optimization

### Database Indexing:
Add indexes for frequently queried fields:
```python
# In models.py
class Donor(db.Model):
    # ...
    __table_args__ = (
        db.Index('idx_organ_type', 'organ_type'),
        db.Index('idx_blood_group', 'blood_group'),
    )
```

### Caching:
Install Flask-Caching:
```bash
pip install Flask-Caching
```

```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/matches')
@cache.cached(timeout=300)  # Cache for 5 minutes
def matches():
    # ...
```

---

## 9. Minimum System Requirements

### For Small Clinics (< 1000 records):
- CPU: 2 cores
- RAM: 2GB
- Storage: 10GB
- OS: Linux (Ubuntu 20.04+)

### For Large Hospitals (> 10,000 records):
- CPU: 4+ cores
- RAM: 8GB+
- Storage: 50GB+
- Database: PostgreSQL on separate server

---

## 10. Quick Production Checklist

Before going live, verify:

- [ ] SESSION_SECRET set to strong random value
- [ ] FLASK_DEBUG=false
- [ ] Using production WSGI server (Gunicorn/uWSGI)
- [ ] PostgreSQL configured (if needed)
- [ ] HTTPS enabled via reverse proxy
- [ ] Secure cookie flags enabled
- [ ] File upload limits configured
- [ ] Backup strategy implemented
- [ ] Monitoring/logging configured
- [ ] Database indexes created
- [ ] All environment variables documented
- [ ] Health check endpoint added

---

## 11. Health Check Endpoint (Optional)

Add to `app.py`:
```python
@app.route('/health')
def health():
    try:
        # Check database
        Donor.query.first()
        # Check model
        model, _ = load_model()
        return jsonify({
            'status': 'healthy',
            'database': 'ok',
            'model': 'loaded' if model else 'missing'
        }), 200
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500
```

---

## 12. Example Production Startup Script

**`start_production.sh`:**
```bash
#!/bin/bash
set -e

# Load environment variables
export SESSION_SECRET="$(cat /secure/secret.key)"
export FLASK_DEBUG=false
export DATABASE_URL="postgresql://user:pass@localhost/organmatch"

# Start with Gunicorn
gunicorn -w 4 \
         -b 0.0.0.0:5000 \
         --reuse-port \
         --access-logfile logs/access.log \
         --error-logfile logs/error.log \
         --log-level info \
         app:app
```

---

## 13. Testing Production Setup

Before deployment:

```bash
# Test with production config
FLASK_DEBUG=false SESSION_SECRET=test123456789012345678901234567890 python app.py

# Load test
pip install locust
locust -f locustfile.py --host=http://localhost:5000
```

---

## Support

For production deployment issues:
- Check logs first: `tail -f logs/error.log`
- Verify environment variables: `env | grep FLASK`
- Test database connection
- Confirm model file exists: `ls -lh models/random_forest.joblib`

---

**Remember**: Never deploy with debug mode enabled or default SECRET_KEY!
