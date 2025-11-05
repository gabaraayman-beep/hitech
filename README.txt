MyApp - Simple Flask app (Login / Signup / Dashboard)
======================================================

How it works
------------
- Users register via Sign Up. Username should match the image filename you will place in /static (e.g. 101 -> /static/101.jpg).
- On login, the dashboard shows the image at /static/{username}.jpg. To update an image, replace the file on the server with the same filename.
- Database: SQLite file `database.db` will be created on first run and pre-populated with two sample users:
  - username: 101  password: 1234
  - username: 102  password: 5678

Run locally
-----------
1. Make sure Python and pip are installed. Install requirements:
   pip install flask werkzeug pillow

2. Run:
   python app.py

3. Open browser: http://127.0.0.1:5000

Notes
-----
- This project is for local development/demo. For production use a proper WSGI server and secure secret key.
- The default images are generated as placeholders. Replace /static/{username}.jpg with your monthly images keeping the same filename.
