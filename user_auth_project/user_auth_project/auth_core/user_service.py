import sqlite3
from user_db import DB_NAME,init_db 

init_db()

def register_user(username, password):
    if not username or not password:
        return "Missing fields"

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return "User already exists"

    cursor.execute(f"INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    return "User registered"

def authenticate_user(username, password):
    if not username or not password:
        return "Missing credentials"
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    return "Login success" if user else "Invalid credentials"

res=register_user("newtestuser2", "newtestpass")
print(res)
