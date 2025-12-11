# 🚀 OrganMatch Deployment Guide

This guide covers deploying OrganMatch to various platforms and environments.

## Table of Contents
1. [Quick Deploy with Docker](#quick-deploy-with-docker)
2. [Deploy to Heroku](#deploy-to-heroku)
3. [Deploy to AWS](#deploy-to-aws)
4. [Deploy to Digital Ocean](#deploy-to-digital-ocean)
5. [Deploy to Railway](#deploy-to-railway)
6. [Deploy to Render](#deploy-to-render)

---

## Quick Deploy with Docker

### Prerequisites
- Docker installed
- Docker Compose installed

### Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd organmatch
```

2. **Set environment variables**
```bash
cp .env.example .env
# Edit .env and set your SECRET_KEY
python -c "import secrets; print(secrets.token_hex(32))"
```

3. **Build and run with Docker Compose**
```bash
docker-compose up -d
```

4. **Access the application**
- Open browser to `http://localhost:5000`
- Default credentials will be created on first run

5. **View logs**
```bash
docker-compose logs -f web
```

6. **Stop the application**
```bash
docker-compose down
```

---

## Deploy to Heroku

### Prerequisites
- Heroku CLI installed
- Heroku account

### Steps

1. **Login to Heroku**
```bash
heroku login
```

2. **Create new Heroku app**
```bash
heroku create organmatch-app
```

3. **Add PostgreSQL addon**
```bash
heroku addons:create heroku-postgresql:mini
```

4. **Set environment variables**
```bash
heroku config:set SESSION_SECRET=$(python -c "import secrets; print(secrets.token_hex(32))")
heroku config:set FLASK_ENV=production
```

5. **Deploy**
```bash
git push heroku main
```

6. **Initialize database**
```bash
heroku run python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

7. **Open application**
```bash
heroku open
```

### Monitoring
```bash
heroku logs --tail
heroku ps
```

---

## Deploy to Railway

### Prerequisites
- Railway account
- Railway CLI (optional)

### Via Railway Dashboard

1. **Connect Repository**
   - Go to Railway dashboard
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

2. **Add PostgreSQL Database**
   - Click "New" → "Database" → "PostgreSQL"
   - Railway will automatically set DATABASE_URL

3. **Set Environment Variables**
   - Go to your service settings
   - Add environment variables:
     - `SESSION_SECRET`: Generate with `python -c "import secrets; print(secrets.token_hex(32))"`
     - `FLASK_ENV`: `production`

4. **Deploy**
   - Railway will automatically detect and deploy your app
   - Access via the generated Railway URL

### Via Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Add PostgreSQL
railway add

# Set environment variables
railway variables set SESSION_SECRET=<your-secret>
railway variables set FLASK_ENV=production

# Deploy
railway up
```

---

## Deploy to Render

### Via Render Dashboard

1. **Create Web Service**
   - Go to Render dashboard
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Configure Service**
   - **Name**: organmatch
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --config gunicorn.conf.py app:app`

3. **Add PostgreSQL Database**
   - Click "New +" → "PostgreSQL"
   - Note the Internal Database URL

4. **Set Environment Variables**
   - Go to your web service → Environment
   - Add:
     - `DATABASE_URL`: Your PostgreSQL Internal URL
     - `SESSION_SECRET`: Generate secure key
     - `FLASK_ENV`: `production`
     - `PYTHON_VERSION`: `3.11.6`

5. **Deploy**
   - Render will automatically build and deploy
   - Access via the generated Render URL

---

## Deploy to AWS (EC2)

### Prerequisites
- AWS account
- EC2 instance running Ubuntu 22.04
- SSH key pair

### Steps

1. **SSH into EC2 instance**
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

2. **Update system and install dependencies**
```bash
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3-pip nginx postgresql postgresql-contrib
```

3. **Create PostgreSQL database**
```bash
sudo -u postgres psql
CREATE DATABASE organmatch;
CREATE USER organmatch WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE organmatch TO organmatch;
\q
```

4. **Clone repository**
```bash
cd /var/www
sudo git clone <your-repo-url> organmatch
cd organmatch
```

5. **Create virtual environment and install dependencies**
```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. **Configure environment**
```bash
cp .env.example .env
nano .env
# Set your environment variables
```

7. **Configure Gunicorn systemd service**
```bash
sudo nano /etc/systemd/system/organmatch.service
```

Add:
```ini
[Unit]
Description=Gunicorn instance for OrganMatch
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/organmatch
Environment="PATH=/var/www/organmatch/venv/bin"
EnvironmentFile=/var/www/organmatch/.env
ExecStart=/var/www/organmatch/venv/bin/gunicorn --config gunicorn.conf.py app:app

[Install]
WantedBy=multi-user.target
```

8. **Configure Nginx**
```bash
sudo nano /etc/nginx/sites-available/organmatch
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /var/www/organmatch/static;
    }
}
```

9. **Enable and start services**
```bash
sudo ln -s /etc/nginx/sites-available/organmatch /etc/nginx/sites-enabled/
sudo systemctl start organmatch
sudo systemctl enable organmatch
sudo systemctl restart nginx
```

10. **Setup SSL with Let's Encrypt (optional)**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## Deploy to Digital Ocean App Platform

### Via DO Dashboard

1. **Create App**
   - Go to Digital Ocean Apps
   - Click "Create App"
   - Choose GitHub and select your repository

2. **Configure Resources**
   - **Type**: Web Service
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `gunicorn --config gunicorn.conf.py app:app`
   - **HTTP Port**: 5000

3. **Add Database**
   - Click "Create Resource" → "Database"
   - Choose PostgreSQL
   - Digital Ocean will automatically set DATABASE_URL

4. **Set Environment Variables**
   - Add in App Settings:
     - `SESSION_SECRET`: Generate secure key
     - `FLASK_ENV`: `production`

5. **Deploy**
   - Click "Create Resources"
   - App will automatically deploy

---

## Production Checklist

Before deploying to production, ensure:

- [ ] `SESSION_SECRET` is set to a strong random value
- [ ] `FLASK_ENV` is set to `production`
- [ ] `DEBUG` is `False`
- [ ] Database is PostgreSQL (not SQLite)
- [ ] All sensitive data is in environment variables
- [ ] SSL/HTTPS is configured
- [ ] Database backups are configured
- [ ] Monitoring and logging are set up
- [ ] Firewall rules are configured
- [ ] Regular security updates are scheduled

---

## Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `SESSION_SECRET` | Yes | Flask secret key | Random 64-char hex string |
| `DATABASE_URL` | Yes | PostgreSQL connection string | `postgresql://user:pass@host:5432/db` |
| `FLASK_ENV` | Yes | Environment | `production` or `development` |
| `PORT` | No | Server port | `5000` (default) |
| `HOST` | No | Server host | `0.0.0.0` (default) |

---

## Troubleshooting

### Database Connection Issues
```bash
# Check DATABASE_URL format
echo $DATABASE_URL

# Test connection
psql $DATABASE_URL
```

### Application Won't Start
```bash
# Check logs
heroku logs --tail  # Heroku
docker-compose logs -f web  # Docker
sudo journalctl -u organmatch -f  # SystemD
```

### Static Files Not Loading
- Ensure nginx is configured correctly
- Check file permissions
- Verify STATIC_URL settings

---

## Support

For issues or questions:
- Open an issue on GitHub
- Check existing documentation
- Review logs for error messages
