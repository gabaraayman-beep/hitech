# MyApp - Flask User Dashboard

## Overview
A simple Flask web application featuring user authentication and personalized dashboards. Users can sign up, log in, and view their associated images stored in the static folder. The dashboard includes interactive zoom and pan functionality for images.

## Project Architecture

### Technology Stack
- **Backend**: Flask (Python 3.11)
- **Database**: SQLite (database.db)
- **Frontend**: HTML templates with vanilla JavaScript
- **Styling**: Custom CSS with dark theme
- **Server**: Flask development server (dev), Gunicorn (production)

### Directory Structure
```
├── app.py                 # Main Flask application
├── database.db            # SQLite database (auto-created)
├── requirements.txt       # Python dependencies
├── templates/             # Jinja2 HTML templates
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
└── static/                # Static assets (CSS, images)
    ├── style.css
    ├── default.jpg        # Default placeholder image
    └── [username].jpg     # User-specific images
```

### Key Features
1. **User Authentication**
   - Secure password hashing using Werkzeug
   - Session-based login management
   - Sample users: 101 (password: 1234), 102 (password: 5678)

2. **Personalized Dashboard**
   - Each user sees their image at `/static/{username}.jpg`
   - Falls back to default.jpg if user image not found
   - Interactive zoom and pan controls

3. **Database**
   - SQLite with auto-initialization on first run
   - Users table: id, username, password (hashed)

## Recent Changes (Nov 5, 2025)
- Imported from GitHub repository
- Configured for Replit environment
- Updated Flask to run on 0.0.0.0:5000 for web preview
- Installed Python 3.11 and dependencies
- Created .gitignore for Python projects
- Set up Flask App workflow for automatic startup
- Renamed requirements.txt.txt to requirements.txt

## Development Setup
- **Port**: 5000 (frontend/webview)
- **Host**: 0.0.0.0 (allows Replit proxy access)
- **Debug Mode**: Enabled in development

## Deployment
- Production server: Gunicorn
- Command: `gunicorn app:app`
- Platform: Configured for Replit deployment
