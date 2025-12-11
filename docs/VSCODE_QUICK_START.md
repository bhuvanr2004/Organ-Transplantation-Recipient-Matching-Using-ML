# 💻 VS Code Quick Start Guide - OrganMatch

This guide will help you set up and run OrganMatch in VS Code in under 5 minutes.

## 📋 Prerequisites

- VS Code installed
- Python 3.11+ installed
- Git installed

## 🚀 Quick Setup (5 Steps)

### 1. Open Project in VS Code

```bash
cd organmatch
code .
```

### 2. Install Recommended Extensions

When you open the project, VS Code will prompt you to install recommended extensions. Click **"Install All"**.

Or manually:
- Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
- Type: `Extensions: Show Recommended Extensions`
- Click "Install Workspace Extension Recommendations"

### 3. Create Virtual Environment

Open integrated terminal (`Ctrl+`` or View → Terminal):

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Select Python Interpreter

- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
- Type: `Python: Select Interpreter`
- Choose: `./venv/bin/python` (or `.\venv\Scripts\python.exe` on Windows)

## 🎯 Running the Application

### Method 1: Debug Mode (Recommended)

1. Press `F5` or click the Run icon in the sidebar
2. Select "Flask: OrganMatch" from the dropdown
3. Application will start with debugger attached
4. Browser opens automatically to `http://localhost:5000`

### Method 2: Terminal

```bash
# Make sure virtual environment is activated
python app.py
```

## 🔧 Setup Environment Variables

1. **Copy example environment file:**
```bash
# Windows (Command Prompt)
copy .env.example .env

# Windows (PowerShell)
Copy-Item .env.example .env

# macOS/Linux
cp .env.example .env
```

2. **Generate secret key:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

3. **Edit .env file:**
   - Open `.env` in VS Code
   - Replace `your-secret-key-here` with the generated key
   - Save the file

## 🐛 Debugging

### Set Breakpoints

1. Click to the left of a line number to set a breakpoint (red dot appears)
2. Press `F5` to start debugging
3. Code will pause at breakpoints
4. Use debug controls:
   - `F10` - Step Over
   - `F11` - Step Into
   - `Shift+F11` - Step Out
   - `F5` - Continue

### Debug Configurations Available

- **Flask: OrganMatch** - Run the main web application
- **Python: Current File** - Debug any Python file
- **Python: Train Model** - Debug the ML model training

### View Variables

When debugging:
- Variables panel shows all local/global variables
- Hover over variables in code to see values
- Use Debug Console to evaluate expressions

## 📁 Workspace Features

### File Explorer

- `Ctrl+Shift+E` - Toggle file explorer
- Right-click for context menu
- Drag and drop to move files

### Search Across Files

- `Ctrl+Shift+F` - Global search
- `Ctrl+H` - Find and replace
- Supports regex and case-sensitive search

### Git Integration

- `Ctrl+Shift+G` - Open Source Control
- Stage changes by clicking `+`
- Commit with `Ctrl+Enter`
- View diff by clicking on changed files

## ⚡ Useful Keyboard Shortcuts

### General
- `Ctrl+P` - Quick file open
- `Ctrl+Shift+P` - Command palette
- `Ctrl+`  - Toggle terminal
- `Ctrl+B` - Toggle sidebar

### Editing
- `Alt+Up/Down` - Move line up/down
- `Shift+Alt+Up/Down` - Copy line up/down
- `Ctrl+/` - Toggle comment
- `Ctrl+D` - Select next occurrence
- `Ctrl+Shift+L` - Select all occurrences

### Python-specific
- `Shift+Enter` - Run Python file in terminal
- `Ctrl+Shift+P` → `Python: Run Python File in Terminal`
- `F5` - Start debugging
- `Shift+F5` - Stop debugging

## 📂 Project Navigation

### Important Files

| File | Description | Shortcut to Open |
|------|-------------|------------------|
| `app.py` | Main Flask application | `Ctrl+P` → type "app" |
| `models.py` | Database models | `Ctrl+P` → type "models" |
| `config.py` | Configuration | `Ctrl+P` → type "config" |
| `.env` | Environment variables | `Ctrl+P` → type ".env" |

### Important Folders

| Folder | Contents |
|--------|----------|
| `templates/` | HTML templates (Jinja2) |
| `static/` | CSS, JavaScript, images |
| `ml/` | Machine learning modules |
| `models/` | Trained ML models |

## 🧪 Testing in VS Code

### Run Tests

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html
```

### View Coverage

- Coverage report generated in `htmlcov/`
- Open `htmlcov/index.html` in browser

## 🎨 Code Formatting

### Auto-format on Save

The project is configured to auto-format Python files with Black when you save.

### Manual Formatting

- Right-click in editor → `Format Document`
- Or: `Shift+Alt+F`

## 📊 Database Viewer

### View SQLite Database

1. Install "SQLite Viewer" extension (already in recommendations)
2. Right-click on `instance/organmatch.db`
3. Select "Open Database"
4. Browse tables and data

## 🔍 Common Issues & Solutions

### Issue: Python interpreter not found

**Solution:**
1. Press `Ctrl+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose the one from your `venv` folder

### Issue: Module not found errors

**Solution:**
```bash
# Make sure virtual environment is activated
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Port 5000 already in use

**Solution:**
```bash
# Find process using port 5000
# Windows
netstat -ano | findstr :5000

# macOS/Linux
lsof -i :5000

# Kill the process or change port in config.py
```

### Issue: Changes not reflecting

**Solution:**
- Stop the server (`Ctrl+C` in terminal)
- Restart with `F5` or `python app.py`
- Hard refresh browser (`Ctrl+Shift+R`)

## 🚀 Next Steps

1. **Read the README**: `Ctrl+P` → type "README"
2. **Explore templates**: Navigate to `templates/` folder
3. **Check ML code**: Look at `ml/` folder
4. **Test the API**: Use REST Client extension or Postman

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [VS Code Debugging](https://code.visualstudio.com/docs/editor/debugging)
- [Git in VS Code](https://code.visualstudio.com/docs/editor/versioncontrol)

## 💡 Tips & Tricks

1. **Multi-cursor editing**: `Alt+Click` to place multiple cursors
2. **Split editor**: `Ctrl+\` to split editor view
3. **Zen mode**: `Ctrl+K Z` for distraction-free coding
4. **Terminal tabs**: Click `+` in terminal to open multiple terminals
5. **Peek definition**: `Alt+F12` to peek at function definitions
6. **Go to definition**: `F12` to jump to definition

---

**Happy Coding! 🎉**

For issues or questions, check the main [README.md](README.md) or [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md).
