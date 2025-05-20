def check_password(password):
    special_chars = "!@#$%^&*"
    pw_len = 8 <= len(password) <= 16

    is_upper = False
    is_lower = False
    is_digit = False
    is_special = False

    for char in password:
        if char.isupper():
            is_upper = True
        elif char.islower():
            is_lower = True
        elif char.isdigit():
            is_digit = True
        elif char in special_chars:
            is_special = True

    if pw_len == False:
        print("error,must be 8-16 characters")
    if is_upper == False:
        print("error,must contain at least one uppercase letter.")
    if is_lower == False:
        print("error,must contain at least one lowercase letter.")
    if is_digit == False:
        print("error,must contain at least one digit.")
    if is_special == False:
        print("error,must contain at least one special character.")
    
    if pw_len and is_upper and is_lower and is_digit and is_special:
        print("Password is valid.")

user_password = input("Enter a password to check: ")
check_password(user_password)
