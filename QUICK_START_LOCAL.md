# OrganMatch - Quick Start Guide for Local Development

This guide will help you get OrganMatch running on your local machine using VS Code.

## Prerequisites

- Python 3.8 or higher
- Git (optional)

## Step-by-Step Setup

### 1. Extract and Open Project

```bash
# Extract the downloaded zip file
tar -xzf OrganMatch_VSCode.tar.gz

# Navigate to the project directory
cd OrganMatch

# Open in VS Code
code .
```

### 2. Create Virtual Environment

Open the terminal in VS Code (Ctrl + ` or View > Terminal) and run:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Database

This crucial step creates the database and loads sample data:

```bash
python init_db.py
```

This script will:
- ✅ Create all database tables
- ✅ Create a test user (admin / admin123)
- ✅ Load sample donor and recipient data
- ✅ Prepare the app for first use

### 5. Run the Application

```bash
python app.py
```

You should see output like:
```
✅ Model already exists, skipping initial training
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

### 6. Access the Application

Open your browser and go to: **http://localhost:5000**

### 7. Login

Use the default test credentials:
- **Username:** admin
- **Password:** admin123

### 8. (Optional) Create Additional Users

If you want to add more users (like "bhuvan"), run:

```bash
python init_db.py --create-user bhuvan bhuvan@organmatch.local password123
```

Replace with your own username, email, and password as needed.

## Features Available Locally

✅ **Add Donors & Recipients** - Manual location entry with latitude/longitude
✅ **View Matches** - AI-powered compatibility matching with 1-10 urgency levels
✅ **Manage Data** - Create, view, and manage all donor/recipient information
✅ **Download Data** - Export donors and recipients as CSV
✅ **View Distances** - See geographical distances between donors and recipients

## Database File Location

When running locally, the database file will be created at:
- **SQLite (default):** `organmatch.db` (in project root)

## Troubleshooting

### Port 5000 Already in Use
Change the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change 5001 to any available port
```

### Database Issues
Reset the database:
```bash
# Delete the existing database
rm organmatch.db

# Reinitialize
python init_db.py
```

### Missing Sample Data
If sample CSV files are missing:
1. Manually add donors/recipients through the UI
2. Or contact the development team for the data files

### ModuleNotFoundError
Ensure virtual environment is activated:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

## Development Tips

### Enable Debug Mode
The app runs in debug mode by default, allowing hot reload on file changes.

### Reset Admin Password
```python
# Run in Python shell
from app import app, db
from models import User

with app.app_context():
    admin = User.query.filter_by(username='admin').first()
    admin.set_password('newpassword123')
    db.session.commit()
```

### View Database Contents
Use any SQLite viewer (e.g., SQLite Browser) to inspect `organmatch.db`

## Next Steps

1. ✅ Explore the dashboard
2. ✅ Add sample donors and recipients
3. ✅ Test the matching algorithm
4. ✅ Experiment with different parameters

## Support

For issues or questions, refer to:
- `PROJECT_DOCUMENTATION.md` - Full technical documentation
- `README.md` - Project overview
- Contact the development team

Happy organ matching! 🏥❤️
