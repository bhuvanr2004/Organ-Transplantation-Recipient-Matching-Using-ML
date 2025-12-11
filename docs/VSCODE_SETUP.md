# Running OrganMatch in VS Code - Complete Setup Guide

This guide will help you run the **OrganMatch** project in Visual Studio Code with all features working: database storage, ML model training, data fetching, and real-time predictions.

---

## Prerequisites

Before starting, make sure you have:

1. **Python 3.8+** installed ([Download Python](https://www.python.org/downloads/))
2. **VS Code** installed ([Download VS Code](https://code.visualstudio.com/))
3. **Git** installed (optional, for cloning)

---

## Step 1: Download the Project

### Option A: Download from Replit
1. In Replit, click the three dots menu (⋮) at the top
2. Select "Download as zip"
3. Extract the zip file to your desired location
4. Open the folder in VS Code: `File > Open Folder`

### Option B: If you have Git access
```bash
git clone <your-repository-url>
cd OrganMatch
code .
```

---

## Step 2: Set Up Python Environment in VS Code

### 2.1 Open the Project in VS Code
- Open VS Code
- Go to `File > Open Folder`
- Select your OrganMatch project folder

### 2.2 Create a Virtual Environment
Open the VS Code terminal (`View > Terminal` or `` Ctrl+` ``) and run:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt.

### 2.3 Install Python Dependencies
With the virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- scikit-learn (ML library)
- pandas, numpy (data processing)
- SQLAlchemy (database)
- geopy (distance calculations)
- and all other dependencies

---

## Step 3: Set Up the Database

The project uses **SQLite** for local development (no setup needed!) and **PostgreSQL** for production.

### Local Development (Recommended for VS Code)
SQLite is file-based and requires no installation. The database file will be automatically created at:
```
instance/organmatch.db
```

### Optional: Use PostgreSQL Locally
If you want to use PostgreSQL (like production):

1. Install PostgreSQL on your machine
2. Create a database:
   ```bash
   createdb organmatch
   ```
3. Set environment variable:
   ```bash
   export DATABASE_URL="postgresql://username:password@localhost/organmatch"
   ```

---

## Step 4: Initialize the Application

### 4.1 Create Required Folders
The app needs these folders (some may already exist):

```bash
mkdir -p models uploads instance
```

### 4.2 First Run - Initialize Database & Train Model
Run the Flask application for the first time:

```bash
python app.py
```

**What happens on first run:**
1. ✅ Creates database tables (Users, Donors, Recipients, etc.)
2. ✅ Loads sample data (10 donors, 8 recipients)
3. ✅ Trains the Random Forest ML model
4. ✅ Saves the model to `models/random_forest.joblib`
5. ✅ Starts the web server on `http://localhost:5000`

You should see output like:
```
🔧 Creating features from donor-recipient pairs...
📊 Training on X samples...
✅ Model trained successfully!
 * Running on http://127.0.0.1:5000
```

---

## Step 5: Access the Application

1. Open your web browser
2. Go to: **http://localhost:5000**
3. You'll see the login page

### Default Test Account
Create a new account or use the registration page:
- Go to `http://localhost:5000/register`
- Create your admin account

---

## Step 6: Test All Features

### ✅ Feature 1: Dashboard
- View: `http://localhost:5000/dashboard`
- Shows: Total donors, recipients, organ distribution charts
- Real-time statistics

### ✅ Feature 2: Add Individual Donor/Recipient
- Donors: `http://localhost:5000/add_donor`
- Recipients: `http://localhost:5000/add_recipient`
- Fill forms with medical data (age, blood group, HLA typing, GPS location, etc.)

### ✅ Feature 3: View All Data
- Donors List: `http://localhost:5000/donors`
- Recipients List: `http://localhost:5000/recipients`
- Tables with all stored records

### ✅ Feature 4: ML Compatibility Matching
- View Matches: `http://localhost:5000/matches`
- See compatibility scores (0-100%) for all donor-recipient pairs
- Color-coded: Green (excellent), Yellow (good), Red (poor)

### ✅ Feature 5: Bulk CSV Upload
- Upload Page: `http://localhost:5000/upload`
- Upload CSV files with multiple donors/recipients at once
- Sample CSV templates available in `data/` folder

### ✅ Feature 6: Model Training & Evaluation
- Evaluate Page: `http://localhost:5000/evaluate`
- View feature importance, confusion matrix, ROC curves
- Click "Retrain Model" button after adding new data

### ✅ Feature 7: Real-Time Location
- Distances Page: `http://localhost:5000/distances`
- See GPS distances between donors and recipients
- Update your location using browser geolocation

### ✅ Feature 8: System Logs
- Logs Page: `http://localhost:5000/logs`
- View all system events (model training, data additions, errors)
- Terminal-style interface with color-coded messages

---

## Step 7: VS Code Recommended Extensions

Install these VS Code extensions for better development:

1. **Python** (by Microsoft) - Python language support
2. **Pylance** - Fast Python intellisense
3. **SQLite Viewer** - View your SQLite database directly in VS Code
4. **Better Jinja** - Syntax highlighting for HTML templates

To install:
- Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on Mac)
- Search for extension name
- Click "Install"

---

## Step 8: Development Workflow in VS Code

### Running the Server
Open VS Code terminal and run:
```bash
# Activate virtual environment first
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Run the app
python app.py
```

### Debug Mode
For better error messages during development:
```bash
FLASK_DEBUG=true python app.py
```

Or create a `.env` file:
```
FLASK_DEBUG=true
SESSION_SECRET=your-secret-key-here
```

### Stop the Server
Press `Ctrl+C` in the terminal

---

## Step 9: Working with the Database

### View SQLite Database in VS Code
1. Install "SQLite Viewer" extension
2. Open `instance/organmatch.db` file
3. You can browse tables: users, donors, recipients, match_history, system_logs

### Reset Database (if needed)
```bash
# Delete the database file
rm instance/organmatch.db

# Run app again to recreate with fresh data
python app.py
```

---

## Step 10: Model Training Workflow

### Automatic Training
The model automatically trains:
- On first run (with sample data)
- When you click "Retrain Model" button in the UI

### Manual Training via Code
You can also retrain programmatically:

```python
from ml.train_model import train_model
from models import Donor, Recipient
import pandas as pd

# Get all data
donors = Donor.query.all()
recipients = Recipient.query.all()

# Convert to DataFrames
donors_df = pd.DataFrame([d.to_dict() for d in donors])
recipients_df = pd.DataFrame([r.to_dict() for r in recipients])

# Train
train_model(donors_df, recipients_df)
```

### Model Location
The trained model is saved at:
```
models/random_forest.joblib
```

---

## Step 11: API Testing

The app provides REST APIs for integration:

### Predict Compatibility
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"donor_id": 1, "recipient_id": 1}'
```

### Retrain Model
```bash
curl -X POST http://localhost:5000/api/retrain
```

---

## Step 12: Adding Sample Data

### Using CSV Upload
1. Go to `http://localhost:5000/upload`
2. Use sample files in `data/` folder:
   - `data/donors_sample.csv`
   - `data/recipients_sample.csv`
3. Upload and the model will auto-retrain

### Using Individual Forms
Add donors/recipients one by one through the web forms for granular control.

---

## Common Issues & Solutions

### Issue 1: "Module not found" errors
**Solution:** Make sure virtual environment is activated
```bash
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### Issue 2: "Port 5000 already in use"
**Solution:** Kill the process or use a different port
```bash
# Use different port
python app.py --port 8000

# Or kill existing process (Mac/Linux)
lsof -ti:5000 | xargs kill -9
```

### Issue 3: Database errors
**Solution:** Delete and recreate database
```bash
rm instance/organmatch.db
python app.py
```

### Issue 4: Model not training
**Solution:** Check you have data in the database
1. Add at least 1 donor and 1 recipient
2. Click "Retrain Model" button
3. Check logs at `http://localhost:5000/logs`

---

## Project File Structure

```
OrganMatch/
├── app.py                      # Main Flask application (START HERE)
├── models.py                   # Database models (User, Donor, Recipient)
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
│
├── ml/                         # Machine Learning code
│   ├── feature_engineering.py  # Feature calculations
│   ├── train_model.py         # Model training logic
│   └── predict_model.py       # Prediction engine
│
├── data/                       # Sample CSV files
│   ├── donors_sample.csv
│   └── recipients_sample.csv
│
├── templates/                  # HTML pages
│   ├── dashboard.html
│   ├── matches.html
│   └── ... (12 more templates)
│
├── static/                     # CSS, JS, images
│   ├── css/theme.css
│   └── js/location.js
│
├── models/                     # Trained ML models (auto-created)
│   ├── random_forest.joblib
│   └── model_config.json
│
├── instance/                   # Database storage (auto-created)
│   └── organmatch.db
│
└── uploads/                    # CSV uploads (auto-created)
```

---

## Next Steps

### For Development:
1. ✅ Modify templates in `templates/` folder
2. ✅ Edit ML parameters in `ml/train_model.py`
3. ✅ Add new features in `app.py`
4. ✅ Customize styling in `static/css/theme.css`

### For Production Deployment:
See `PRODUCTION_SETUP.md` for:
- Gunicorn WSGI server setup
- PostgreSQL migration
- HTTPS configuration
- Security hardening

---

## Summary Checklist

- [ ] Python 3.8+ installed
- [ ] VS Code installed
- [ ] Project folder opened in VS Code
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Flask app running (`python app.py`)
- [ ] Browser opened to `http://localhost:5000`
- [ ] Account created and logged in
- [ ] Dashboard showing data
- [ ] ML model trained successfully

---

## Quick Start (TL;DR)

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open browser to http://localhost:5000
```

That's it! You're now running OrganMatch in VS Code with full functionality! 🎉

---

## Support

If you encounter any issues:
1. Check the **System Logs** page in the app
2. Review the terminal output
3. Verify all dependencies are installed
4. Ensure virtual environment is activated

**Happy matching! 🏥💚**
