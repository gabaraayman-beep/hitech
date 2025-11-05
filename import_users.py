import csv
import sqlite3

# Connect to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        username = row['username']
        password = row['password']
        
        # Check if username already exists
        c.execute('SELECT id FROM users WHERE username = ?', (username,))
        existing = c.fetchone()
        
        if existing:
            # Update existing user's password
            c.execute('UPDATE users SET password = ? WHERE username = ?', (password, username))
            print(f"🔁 Updated password for user: {username}")
        else:
            # Add new user
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            print(f"✅ Added new user: {username}")

conn.commit()
conn.close()

print("🎉 Import completed successfully!")
