import re

def validate_username(username):
    if not username or ' ' in username:
        return False
    return True

def validate_password(password):
    if (len(password) < 8 or
        not re.search(r'\d', password) or
        not re.search(r'[A-Za-z]', password) or
        not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return False
    return True

def validate_email(email):
    if '@' not in email or '.' not in email:
        return False
    return True