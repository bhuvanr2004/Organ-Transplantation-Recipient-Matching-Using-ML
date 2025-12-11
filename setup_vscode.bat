@echo off
REM OrganMatch - VS Code Setup Script (Windows)
REM This script automates the setup process for running OrganMatch locally

echo ===================================
echo OrganMatch - VS Code Setup Script
echo ===================================
echo.

REM Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed. Please install Python 3.8+ first.
    echo         Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo    Found: Python %PYTHON_VERSION%
echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo    Virtual environment created
) else (
    echo    Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo    Virtual environment activated
echo.

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip -q
pip install -r requirements.txt -q
echo    All dependencies installed
echo.

REM Create required directories
echo Creating required directories...
if not exist "models" mkdir models
if not exist "uploads" mkdir uploads
if not exist "instance" mkdir instance
echo    Directories created
echo.

REM Check if database exists
if exist "instance\organmatch.db" (
    echo Database already exists at: instance\organmatch.db
) else (
    echo Database will be created on first run
)
echo.

REM Check if model exists
if exist "models\random_forest.joblib" (
    echo ML model already exists at: models\random_forest.joblib
) else (
    echo ML model will be trained on first run
)
echo.

echo ===================================
echo Setup Complete!
echo.
echo To start the application:
echo   1. Activate virtual environment:
echo      venv\Scripts\activate
echo.
echo   2. Run the Flask app:
echo      python app.py
echo.
echo   3. Open browser to:
echo      http://localhost:5000
echo.
echo For detailed instructions, see: VSCODE_SETUP.md
echo Happy matching!
echo.
pause
