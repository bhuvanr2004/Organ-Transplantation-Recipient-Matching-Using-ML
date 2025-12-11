@echo off
REM Quick run script for OrganMatch (Windows)

REM Activate virtual environment
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo Virtual environment activated
) else (
    echo [ERROR] Virtual environment not found. Run setup_vscode.bat first.
    pause
    exit /b 1
)

REM Check if dependencies are installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo [ERROR] Dependencies not installed. Run setup_vscode.bat first.
    pause
    exit /b 1
)

echo ===================================
echo Starting OrganMatch...
echo Server will run at: http://localhost:5000
echo Press Ctrl+C to stop
echo ===================================
echo.

REM Run the Flask app
python app.py
