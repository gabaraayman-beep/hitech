from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'database.db'
app = Flask(__name__)
app.secret_key = 'replace-this-with-a-secret-key'  # change this in production

def init_db():
    created = False
    if not DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )""")
        # Add sample users (username numeric as requested)
        from werkzeug.security import generate_password_hash
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?,?)", ('101', generate_password_hash('1234')))
            c.execute("INSERT INTO users (username, password) VALUES (?,?)", ('102', generate_password_hash('5678')))
        except Exception:
            pass
        conn.commit()
        conn.close()
        created = True
    return created

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def setup():
    init_db()
    static_folder = BASE_DIR / 'static'
    static_folder.mkdir(exist_ok=True)

# شغّل setup() مرة واحدة مباشرة بعد تعريفه
setup()


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username','').strip()
        password = request.form.get('password','').strip()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cur.fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username','').strip()
        password = request.form.get('password','').strip()
        if not username or not password:
            flash('Please provide username and password', 'warning')
            return render_template('signup.html')
        # username should be filename-friendly; user said username is the image name
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (?,?)",
                        (username, generate_password_hash(password)))
            conn.commit()
            flash('Account created. You can now log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Username already exists or invalid. Choose another.', 'danger')
            return render_template('signup.html')
        finally:
            conn.close()
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('user')
    if not username:
        return redirect(url_for('login'))
    # The image path is always /static/{username}.jpg as requested
    image_url = f"/static/{username}.jpg"
    # Check if file exists; if not, show a default placeholder
    img_path = BASE_DIR / 'static' / f"{username}.jpg"
    if not img_path.exists():
        image_url = "/static/default.jpg"
    return render_template('dashboard.html', username=username, image_url=image_url)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

