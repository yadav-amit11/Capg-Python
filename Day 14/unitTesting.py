USERS={
    "admin":"admin123",
    "john":"johnpass",
    "alice":"alice123"
}
def authentication(username,password):
    if not username or not password:
        return "missing credentials"
    if username in USERS and USERS[username]==password:
        return "logged in"
    return "invalid creds"
    
print(authentication("", "")) #missing credentials
print(authentication("admin", "admin123")) #logged in
print(authentication("john", "wrongpass")) #invalid creds

