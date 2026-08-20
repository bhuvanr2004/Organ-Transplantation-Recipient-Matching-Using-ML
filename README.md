# 🫀Organ Transplantation & Recipient Matching Using ML 

##OrganMatch - AI-Powered Organ Donation Matching Platform

A production-ready, full-stack web application that uses **Machine Learning** to predict donor-recipient compatibility for organ transplants. Built with Flask, SQLAlchemy, scikit-learn, and modern web technologies.

**Status:** Production-Ready | **Version:** 1.0 | **License:** MIT

## ⚠️ IMPORTANT NOTICE

The `app.py file` and `ml-folder` directory has been **intentionally removed** to protect the project’s intellectual work and to prevent unauthorized reuse of the complete implementation.

For **legitimate academic, research, or project-related access** to the full source code, please contact:

- **Email:** bhuvankumarr2004@gmail.com  
- **Phone:** +91 86606 877802



---

## 📑 Table of Contents

1. [Project Overview](#project-overview)
2. [Why This Tech Stack](#why-this-tech-stack)
3. [Frontend Architecture](#-frontend-architecture)
4. [Backend Architecture](#-backend-architecture)
5. [Machine Learning System](#-machine-learning-system)
6. [Project File Structure](#project-file-structure)
7. [Installation & Setup](#installation--setup)
8. [Running the Application](#running-the-application)
9. [Deployment](#deployment)

---

## Project Overview

### What Does OrganMatch Do?

OrganMatch is an intelligent matching system for organ transplants. It:
- **Stores donor and recipient information** securely
- **Analyzes 12+ medical parameters** for each potential match
- **Predicts compatibility scores** (0-100%) using AI/ML
- **Visualizes results** with interactive dashboards
- **Automatically retrains** when new data is added
- **Tracks system events** with comprehensive logging

### Problem Statement

Manual organ matching is:
- ❌ Time-consuming (requires medical staff review)
- ❌ Subjective (depends on individual expertise)
- ❌ Error-prone (human oversight required)
- ❌ Inflexible (hard to analyze all combinations)

### Our Solution

OrganMatch uses **Random Forest Machine Learning** to:
- ✅ Analyze all possible donor-recipient combinations instantly
- ✅ Provide data-driven compatibility predictions
- ✅ Improve outcomes through consistent analysis
- ✅ Learn from historical data automatically

---

## Why This Tech Stack

### Tech Stack Summary

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (Client-Side)                   │
│  HTML5 + CSS3 + JavaScript + Bootstrap 5 + Chart.js         │
└─────────────────────────────────────────────────────────────┘
                            ↕ (HTTP Requests)
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND (Server-Side)                     │
│     Flask 3.0 + Flask-SQLAlchemy + Flask-Login              │
│     SQLAlchemy ORM + Werkzeug Security                       │
└─────────────────────────────────────────────────────────────┘
                            ↕ (SQL Queries)
┌─────────────────────────────────────────────────────────────┐
│                    DATABASE (Data Persistence)                │
│    PostgreSQL (Production) / SQLite (Development)            │
└─────────────────────────────────────────────────────────────┘
                            ↕ (Python Imports)
┌─────────────────────────────────────────────────────────────┐
│              MACHINE LEARNING (AI Intelligence)               │
│   scikit-learn + pandas + numpy + geopy + joblib            │
└─────────────────────────────────────────────────────────────┘
```

### Language Choices & Rationale

#### **Python (Backend & ML)**

**Why Python?**
1. **ML Libraries:** scikit-learn, TensorFlow, pandas are Python-native with excellent support
2. **Data Processing:** pandas is the gold standard for data manipulation and analysis
3. **Rapid Development:** Compared to Java/C++, Python reduces development time by 40-50%
4. **Community:** Largest ML/AI community; thousands of libraries and tutorials
5. **Hospital Integration:** Many healthcare systems already use Python (interoperability)
6. **Readability:** Code clarity is crucial for medical applications (security audits, compliance)

**Python Versions Used:**
- Python 3.11+: Modern async support, faster performance, better typing

#### **HTML5 (Markup)**

**Why HTML5?**
1. **Semantic Structure:** Proper document structure for accessibility (WCAG 2.1 compliance)
2. **Form Validation:** Native input validation (email, number, required fields)
3. **Geolocation API:** Built-in browser location services (no external plugin needed)
4. **Accessibility:** ARIA labels for screen readers (essential for medical apps)
5. **Standards:** Universal browser support without vendor lock-in

#### **CSS3 (Styling)**

**Why CSS3?**
1. **Glassmorphism Design:** Modern aesthetic with backdrop-filter blur effects
2. **Gradients:** Smooth color transitions for professional appearance
3. **Responsive Grid:** CSS Grid + Flexbox for mobile-first design
4. **Animations:** Smooth transitions without JavaScript overhead
5. **Variables:** CSS custom properties for theme consistency

#### **JavaScript (Interactivity)**

**Why Vanilla JS + Libraries?**
1. **Geolocation:** `navigator.geolocation.getCurrentPosition()` for GPS location capture
2. **Fetch API:** Modern alternative to XMLHttpRequest (async/await support)
3. **DOM Manipulation:** Direct access to HTML elements for real-time UI updates
4. **Chart.js:** Lightweight charting library (only 50KB) vs heavy alternatives
5. **OpenStreetMap:** Free, open-source map provider (no API key needed)

#### **Flask (Web Framework)**

**Why Flask?**
1. **Lightweight:** Only 600 lines of core code (vs Django's 10,000+ lines)
2. **Microframework:** Perfect for focused applications (not overkill like Django)
3. **Jinja2 Templating:** Elegant syntax for HTML templates with logic
4. **Extensibility:** Large ecosystem of Flask extensions (Flask-Login, Flask-SQLAlchemy, etc.)
5. **Learning Curve:** Easier for small teams; less magic than Django
6. **Performance:** Faster request handling for matching engine (critical for real-time predictions)

#### **SQLAlchemy (ORM - Object Relational Mapping)**

**Why SQLAlchemy?**
1. **Database Abstraction:** Write code once, run on PostgreSQL/SQLite/MySQL without changes
2. **Type Safety:** Python types mapped to database types (prevents SQL injection)
3. **Relationships:** Easy many-to-one, one-to-many relationships without manual joins
4. **Query Building:** Pythonic syntax instead of raw SQL strings
5. **Migrations:** Works with Alembic for database version control

**Example:**
```python
# SQLAlchemy (Pythonic)
donors = Donor.query.filter_by(blood_group='O+').all()

# vs Raw SQL (Error-prone)
donors = db.execute("SELECT * FROM donors WHERE blood_group='O+'")
```

#### **PostgreSQL (Production Database)**

**Why PostgreSQL?**
1. **ACID Compliance:** Medical data requires guaranteed consistency (no data loss)
2. **JSON Support:** Can store complex medical records without extra tables
3. **Advanced Features:** Window functions, CTEs for complex medical queries
4. **Reliability:** Battle-tested in healthcare systems worldwide
5. **Open Source:** Free, no licensing costs; community support

**Development Database: SQLite**
- Minimal setup (single file: `organmatch.db`)
- Perfect for testing, no database server needed
- Automatically switches to PostgreSQL in production

#### **scikit-learn (Machine Learning)**

**Why scikit-learn?**
1. **Random Forest:** Perfect algorithm for medical predictions (handles missing data)
2. **Evaluation Tools:** Built-in confusion matrix, ROC curves, classification reports
3. **Preprocessing:** Train/test split, feature scaling, imputation
4. **Production Ready:** Serializable models, works in production environments
5. **Interpretability:** Feature importance rankings (doctors want to know why)

**Why NOT Deep Learning (TensorFlow)?**
- Requires massive datasets (millions of samples)
- "Black box" predictions (unacceptable in healthcare)
- Overkill for structured medical data
- Our dataset: ~100-500 donor/recipient pairs (Random Forest is optimal)

---

# 🎨 FRONTEND ARCHITECTURE

The frontend is the user-facing layer. It's responsible for:
- ✅ Capturing user input (forms)
- ✅ Displaying data (tables, charts, maps)
- ✅ Managing navigation
- ✅ Styling and UX

### Frontend Technology Stack

| Technology | Version | Purpose | Why? |
|-----------|---------|---------|------|
| **HTML5** | Latest | Document structure | Semantic markup, accessibility |
| **CSS3** | Latest | Styling & animations | Gradients, backdrop-filter, responsive grid |
| **JavaScript** | ES6+ | Interactivity | Geolocation, fetch requests, DOM manipulation |
| **Bootstrap 5** | 5.3.0 | UI Framework | Pre-built components, responsive grid, icons |
| **Chart.js** | Latest | Data visualization | Lightweight, interactive charts |
| **Font Awesome** | 6.4.0 | Icons | 2000+ medical/UI icons |
| **Leaflet.js** | 1.9.4 | Map visualization | Open-source map library (no API key) |
| **Jinja2** | Built-in | Template engine | Server-side HTML rendering |

---



## 🔧 BACKEND ARCHITECTURE

The backend is the server-side logic. It handles:
- ✅ User authentication
- ✅ Database operations (CRUD)
- ✅ Business logic (matching, predictions)
- ✅ API endpoints
- ✅ Background tasks (model retraining)

### Backend Technology Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Flask** | 3.0.0 | Web framework, routing |
| **Flask-Login** | 0.6.3 | User session management |
| **Flask-SQLAlchemy** | 3.1.1 | Database ORM |
| **SQLAlchemy** | 2.0.23 | ORM library |
| **Werkzeug** | 3.0.1 | Password hashing, utilities |
| **psycopg2-binary** | 2.9.9 | PostgreSQL adapter |
| **pandas** | 2.1.3 | Data processing |
| **geopy** | 2.4.1 | Distance calculations |

---


# 🤖 MACHINE LEARNING SYSTEM

The ML system is the "brain" of OrganMatch. It learns from historical data to predict compatibility.

### ML Technology Stack

| Technology | Purpose |
|-----------|---------|
| **scikit-learn** | Random Forest algorithm, metrics |
| **pandas** | Data processing (DataFrames) |
| **numpy** | Numerical operations |
| **geopy** | Geodesic distance calculation |
| **joblib** | Model serialization (save/load) |

---


## 📊 Project File Structure

```
organmatch/
├── 📄 app.py                          # Main Flask application (1016 lines)
├── 📄 models.py                       # Database models (141 lines)
├── 📄 config.py                       # Environment configuration (73 lines)
├── 📄 requirements.txt                # Python dependencies
├── 📄 gunicorn.conf.py                # Production server config
├── 📄 docker-compose.yml              # Docker orchestration
├── 📄 Dockerfile                      # Container specification
├── 📄 Procfile                        # Heroku deployment config
├── 📄 runtime.txt                     # Python version specification
├── 📄 README.md                       # This file
│
├── 📁 templates/                      # HTML templates (Jinja2)
│   ├── base.html                      # Master template (navigation, footer)
│   ├── login.html                     # Login form
│   ├── register.html                  # Registration form
│   ├── dashboard.html                 # System overview with stats
│   ├── add_donor.html                 # Single donor registration form
│   ├── add_recipient.html             # Single recipient registration form
│   ├── donors.html                    # Donor listing table
│   ├── recipients.html                # Recipient listing table
│   ├── upload.html                    # CSV bulk upload form
│   ├── upload_summary.html            # Upload confirmation page
│   ├── matches.html                   # ML prediction results (color-coded)
│   ├── distances.html                 # GPS distance matrix
│   ├── evaluate.html                  # ML model metrics (confusion matrix, ROC curve)
│   ├── settings.html                  # ML hyperparameter configuration
│   └── logs.html                      # System event logs (terminal-style)
│
├── 📁 static/                         # Static files (CSS, JavaScript, images)
│   ├── css/
│   │   └── theme.css                  # Global styling (glassmorphism, gradients)
│   ├── js/
│   │   └── location.js                # Geolocation functionality (137 lines)
│   ├── medical_bg.jpg                 # Hero background image
│   └── [stock images]                 # Medical/healthcare images
│
├── 📁 ml/                             # Machine Learning modules
│   ├── feature_engineering.py         # Feature creation (12 features per pair)
│   ├── train_model.py                 # Model training & evaluation
│   └── predict_model.py               # Making predictions
│
├── 📁 models/                         # Serialized ML models & config
│   ├── random_forest.joblib           # Trained Random Forest model
│   └── model_config.json              # Hyperparameters (n_estimators, max_depth, etc.)
│
├── 📁 data/                           # Sample data for initialization
│   ├── donors_sample.csv              # Sample donor data (~100 rows)
│   └── recipients_sample.csv          # Sample recipient data (~100 rows)
│
├── 📁 instance/                       # Instance-specific files
│   └── organmatch.db                  # SQLite database (development only)
│
├── 📁 uploads/                        # User uploaded CSV files (temporary)
│
├── 📁 docs/                           # Documentation
│   ├── DEPLOYMENT_GUIDE.md            # Deployment instructions
│   ├── DEVELOPER_HANDOVER.md          # Developer notes
│   ├── QUICK_START.md                 # Quick setup guide
│   └── [other guides]
│
└── 📁 .vscode/                        # VS Code configuration
    ├── launch.json                    # Debug configurations
    └── settings.json                  # Editor settings
```

---

## Installation & Setup

### Prerequisites
- Python 3.11+
- PostgreSQL (production) or SQLite (development)
- git, pip, virtualenv

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/organmatch.git
cd organmatch
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Environment Variables
```bash
# Create .env file
cp .env.example .env

# Edit .env and add:
SESSION_SECRET=<your-secret-key>  # Generate: python -c "import secrets; print(secrets.token_hex(32))"
DATABASE_URL=sqlite:///organmatch.db  # Development
FLASK_ENV=development
```

### Step 5: Initialize Database
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Step 6: Run Application
```bash
python app.py
```

Visit: `http://localhost:5000`

---

## Running the Application

### Development Mode
```bash
export FLASK_ENV=development
python app.py
```

### Production Mode (Gunicorn)
```bash
gunicorn --config gunicorn.conf.py app:app
```

### Docker
```bash
docker-compose up -d
```

---

## Deployment

### Replit (Recommended)
- Already configured with Autoscale deployment
- Just click "Deploy" button
- Automatic PostgreSQL database

### Heroku
```bash
heroku login
heroku create organmatch-app
heroku addons:create heroku-postgresql:mini
git push heroku main
```

### Railway
```bash
railway login
railway init
railway up
```

See `docs/DEPLOYMENT_GUIDE.md` for detailed instructions.

---

## Summary

OrganMatch is a complete, production-ready organ donation matching system built with modern web technologies:

- **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (Geolocation), Bootstrap 5, Chart.js
- **Backend:** Python Flask, SQLAlchemy ORM, PostgreSQL/SQLite
- **ML:** scikit-learn Random Forest, pandas, numpy, geopy
- **DevOps:** Docker, Gunicorn, environment-based configuration

Every file serves a specific purpose, and together they create a system that could genuinely impact transplant outcomes in real hospitals.

---

**Created:** December 2025  
**License:** MIT  
**Maintainers:** [Bhuvan Kumar R]
