# auth_service.py
USERS = {
    "admin": "admin123",
    "john": "johnpass",
    "alice": "alicepwd"
}

def authenticate(username, password):
    if not username or not password:
        return "Missing credentials"
    if username in USERS and USERS[username] == password:
        return "Login success"
    return "Invalid credentials"
