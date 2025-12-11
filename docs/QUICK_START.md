# 🚀 OrganMatch - Quick Start Guide for VS Code

## Super Quick Setup (3 Steps!)

### Step 1: Setup
**Windows:**
```bash
setup_vscode.bat
```

**Mac/Linux:**
```bash
chmod +x setup_vscode.sh
./setup_vscode.sh
```

### Step 2: Run
**Windows:**
```bash
run.bat
```

**Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

### Step 3: Open Browser
Go to: **http://localhost:5000**

---

## Manual Setup (If Scripts Don't Work)

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python app.py

# 5. Open http://localhost:5000
```

---

## What You Get

### ✅ Automatic Features on First Run:
- Creates SQLite database (`instance/organmatch.db`)
- Loads sample data (10 donors, 8 recipients)
- Trains Random Forest ML model
- Saves model to `models/random_forest.joblib`
- Starts web server on port 5000

### 📊 Available Pages:
1. **Dashboard** - `/dashboard` - Overview & statistics
2. **Add Donor** - `/add_donor` - Individual donor form
3. **Add Recipient** - `/add_recipient` - Individual recipient form
4. **Donors List** - `/donors` - View all donors
5. **Recipients List** - `/recipients` - View all recipients
6. **Matches** - `/matches` - ML compatibility scores
7. **Upload** - `/upload` - Bulk CSV upload
8. **Evaluate** - `/evaluate` - Model metrics & feature importance
9. **Distances** - `/distances` - GPS distances
10. **Settings** - `/settings` - ML model configuration
11. **Logs** - `/logs` - System event logs

### 🔬 ML Features Working:
- ✅ Random Forest training (100 trees)
- ✅ Feature engineering (11 features)
- ✅ Compatibility prediction (0-100%)
- ✅ Automatic retraining
- ✅ Missing data handling
- ✅ Model evaluation metrics

### 💾 Database Features:
- ✅ SQLite (local development)
- ✅ PostgreSQL support (production)
- ✅ Auto-migration scripts
- ✅ Persistent storage
- ✅ Relationship management

### 📡 Data Operations:
- ✅ Individual registration forms
- ✅ Bulk CSV upload
- ✅ Real-time location updates
- ✅ Distance calculations (geopy)
- ✅ HLA matching
- ✅ Blood type compatibility

---

## VS Code Features

### Recommended Extensions (Auto-suggested):
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- SQLite Viewer (alexcvzz.vscode-sqlite)
- Jinja (samuelcolvin.jinjahtml)

### Debug Configurations:
Press `F5` in VS Code to:
- Run Flask with debugging
- Run current Python file
- Train ML model standalone

### View Database:
1. Install "SQLite Viewer" extension
2. Right-click `instance/organmatch.db`
3. Select "Open Database"

---

## Common Commands

### Activate Virtual Environment
```bash
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### Run Server
```bash
python app.py
```

### Run with Debug Mode
```bash
FLASK_DEBUG=true python app.py  # Mac/Linux
set FLASK_DEBUG=true && python app.py  # Windows
```

### Reset Database
```bash
rm instance/organmatch.db  # Mac/Linux
del instance\organmatch.db  # Windows
python app.py  # Will recreate
```

### Retrain Model Manually
Open browser and click "Retrain Model" button, or:
```bash
curl -X POST http://localhost:5000/api/retrain
```

---

## File Structure

```
OrganMatch/
├── app.py                 ⭐ Main application (start here)
├── models.py              📊 Database models
├── requirements.txt       📦 Dependencies
├── ml/                    🤖 Machine learning code
├── data/                  📁 Sample CSV files
├── templates/             🎨 HTML pages
├── static/                🖼️ CSS, JS, images
├── models/                💾 Trained ML models (auto-created)
└── instance/              🗄️ SQLite database (auto-created)
```

---

## Testing All Features

### 1. Login/Register
- Create account at `/register`
- Login at `/login`

### 2. View Dashboard
- See total counts and charts
- Check organ distribution

### 3. Add Data
- Add individual donor/recipient via forms
- Or upload CSV from `data/` folder

### 4. View Matches
- See ML predictions (0-100% compatibility)
- Color-coded scores (green/yellow/red)

### 5. Check Model Performance
- Go to `/evaluate`
- View feature importance
- See confusion matrix & ROC curve

### 6. Test Location Features
- Go to `/distances`
- Click "Update My Location"
- See GPS distances

### 7. Retrain Model
- Click "Retrain Model" button
- Check `/logs` for training output

---

## Troubleshooting

### Error: "Module not found"
```bash
# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate
```

### Error: "Port already in use"
```bash
# Kill process
lsof -ti:5000 | xargs kill -9  # Mac/Linux
taskkill /F /IM python.exe     # Windows
```

### Error: Database locked
```bash
# Close all connections and restart
rm instance/organmatch.db
python app.py
```

### Model not predicting
1. Check you have data: Visit `/donors` and `/recipients`
2. Retrain model: Click button in UI or visit `/api/retrain`
3. Check logs: Visit `/logs`

---

## API Endpoints

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

### Update Location
```bash
curl -X POST http://localhost:5000/api/update_location/donor/1 \
  -H "Content-Type: application/json" \
  -d '{"latitude": 40.7128, "longitude": -74.0060}'
```

---

## Next Steps

### Development:
- ✏️ Edit templates in `templates/`
- 🎨 Modify styles in `static/css/theme.css`
- 🔧 Adjust ML parameters in `/settings` page
- 📝 Add custom features in `app.py`

### Production:
- 📖 Read `PRODUCTION_SETUP.md`
- 🗄️ Migrate to PostgreSQL
- 🔒 Set up HTTPS
- 🚀 Deploy with Gunicorn

---

## Support Files

- **VSCODE_SETUP.md** - Detailed setup instructions
- **PRODUCTION_SETUP.md** - Production deployment
- **DEVELOPER_HANDOVER.md** - Technical documentation
- **README.md** - Project overview

---

## Summary

✅ **Setup:** Run `setup_vscode.bat` or `./setup_vscode.sh`  
✅ **Run:** Run `run.bat` or `./run.sh`  
✅ **Access:** Open `http://localhost:5000`  
✅ **Features:** All working (ML, database, location, upload)

**That's it! Happy coding! 🏥💚**
