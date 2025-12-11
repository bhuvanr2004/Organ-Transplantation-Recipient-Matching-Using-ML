#!/bin/bash
# Quick run script for OrganMatch (Mac/Linux)

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✓ Virtual environment activated"
else
    echo "❌ Virtual environment not found. Run setup_vscode.sh first."
    exit 1
fi

# Check if dependencies are installed
python -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Dependencies not installed. Run setup_vscode.sh first."
    exit 1
fi

echo "🏥 Starting OrganMatch..."
echo "📍 Server will run at: http://localhost:5000"
echo "Press Ctrl+C to stop"
echo ""

# Run the Flask app
python app.py
