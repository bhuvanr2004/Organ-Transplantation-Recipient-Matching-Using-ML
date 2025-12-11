# OrganMatch Documentation

Welcome to the OrganMatch documentation! This folder contains comprehensive guides for setting up, developing, and deploying the OrganMatch platform.

## Quick Navigation

### Getting Started
- **[QUICK_START.md](QUICK_START.md)** - Get up and running in 5 minutes
- **[VSCODE_QUICK_START.md](VSCODE_QUICK_START.md)** - VS Code setup in 3 steps

### Development Guides
- **[VSCODE_SETUP.md](VSCODE_SETUP.md)** - Complete VS Code development environment setup
- **[VS_CODE_READY.md](VS_CODE_READY.md)** - VS Code readiness checklist
- **[DEVELOPER_HANDOVER.md](DEVELOPER_HANDOVER.md)** - Complete developer handover guide
- **[SETUP_SUMMARY.md](SETUP_SUMMARY.md)** - System setup summary

### Deployment & Production
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Deploy to Heroku, Railway, Render, or Replit
- **[PRODUCTION_SETUP.md](PRODUCTION_SETUP.md)** - Production environment configuration

### Features
- **[VIEW_LOCATION_FEATURE.md](VIEW_LOCATION_FEATURE.md)** - Real-time location tracking documentation

## Quick Links by Use Case

### "I want to run this locally in VS Code"
1. Read [VSCODE_QUICK_START.md](VSCODE_QUICK_START.md)
2. Follow the 3-step setup process
3. Start developing!

### "I want to deploy to production"
1. Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
2. Choose your platform (Replit, Heroku, Railway, or Render)
3. Follow the platform-specific instructions

### "I'm a new developer taking over this project"
1. Read [DEVELOPER_HANDOVER.md](DEVELOPER_HANDOVER.md)
2. Review [QUICK_START.md](QUICK_START.md)
3. Set up your environment with [VSCODE_SETUP.md](VSCODE_SETUP.md)

### "I just want to try it out quickly"
1. Read [QUICK_START.md](QUICK_START.md)
2. Run the startup script
3. Open http://localhost:5000

## Project Overview

OrganMatch is an AI-powered organ donation matching platform that uses Machine Learning (Random Forest) to predict donor-recipient compatibility. Built with Flask, PostgreSQL, and scikit-learn.

### Key Technologies
- **Backend**: Flask (Python)
- **Database**: PostgreSQL / SQLite
- **Machine Learning**: scikit-learn (Random Forest)
- **Frontend**: Bootstrap 5, Chart.js
- **Deployment**: Gunicorn, Docker support

### Main Features
- AI-powered compatibility matching
- Real-time location tracking
- Bulk CSV upload
- Interactive dashboard
- Model evaluation & metrics
- Automatic model retraining

## Support

For issues or questions:
1. Check the relevant documentation above
2. Review the main [README.md](../README.md)
3. Check the code comments in source files

## File Structure

```
docs/
├── README.md                      # This file
├── QUICK_START.md                # Quick setup guide
├── VSCODE_QUICK_START.md         # VS Code quick setup
├── VSCODE_SETUP.md               # Complete VS Code setup
├── VS_CODE_READY.md              # VS Code readiness
├── DEPLOYMENT_GUIDE.md           # Deployment instructions
├── PRODUCTION_SETUP.md           # Production configuration
├── DEVELOPER_HANDOVER.md         # Developer guide
├── SETUP_SUMMARY.md              # Setup summary
└── VIEW_LOCATION_FEATURE.md      # Location feature docs
```
