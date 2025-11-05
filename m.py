# migrate_hash_existing.py
import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("SELECT id, username, password FROM users")
rows = c.fetchall()
for uid, username, pwd in rows:
    # إذا كانت الكلمة بالفعل تبدو مهشّرة (تبدأ مثلاً بـ 'pbkdf2:' أو '$'), تجاهلها
    if isinstance(pwd, str) and (pwd.startswith('pbkdf2:') or pwd.startswith('$') or pwd.count('$')>0):
        print(f"🔒 Already hashed: {username}")
        continue
    new_hash = generate_password_hash(str(pwd))
    c.execute("UPDATE users SET password = ? WHERE id = ?", (new_hash, uid))
    print(f"🔁 Migrated {username}")

conn.commit()
conn.close()
print("✅ Migration done.")
