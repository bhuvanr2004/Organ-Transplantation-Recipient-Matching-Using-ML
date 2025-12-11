#!/bin/bash
# OrganMatch - VS Code Setup Script
# This script automates the setup process for running OrganMatch locally

echo "🏥 OrganMatch - VS Code Setup Script"
echo "===================================="
echo ""

# Check Python installation
echo "✓ Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "❌ Python is not installed. Please install Python 3.8+ first."
    echo "   Download from: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo "   Found: Python $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "✓ Creating virtual environment..."
if [ ! -d "venv" ]; then
    $PYTHON_CMD -m venv venv
    echo "   Virtual environment created"
else
    echo "   Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi
echo "   Virtual environment activated"
echo ""

# Install dependencies
echo "✓ Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "   All dependencies installed"
echo ""

# Create required directories
echo "✓ Creating required directories..."
mkdir -p models uploads instance
echo "   Directories created"
echo ""

# Check if database exists
if [ -f "instance/organmatch.db" ]; then
    echo "✓ Database already exists at: instance/organmatch.db"
else
    echo "✓ Database will be created on first run"
fi
echo ""

# Check if model exists
if [ -f "models/random_forest.joblib" ]; then
    echo "✓ ML model already exists at: models/random_forest.joblib"
else
    echo "✓ ML model will be trained on first run"
fi
echo ""

echo "===================================="
echo "✅ Setup Complete!"
echo ""
echo "To start the application:"
echo "  1. Activate virtual environment:"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "     venv\\Scripts\\activate"
else
    echo "     source venv/bin/activate"
fi
echo ""
echo "  2. Run the Flask app:"
echo "     python app.py"
echo ""
echo "  3. Open browser to:"
echo "     http://localhost:5000"
echo ""
echo "📖 For detailed instructions, see: VSCODE_SETUP.md"
echo "🏥 Happy matching!"
echo ""
