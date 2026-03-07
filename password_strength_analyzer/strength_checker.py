import re

def check_password_strength(password):
    
    length = len(password)
    
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = 0

    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


password = input("Enter password to analyze: ")

strength = check_password_strength(password)

print("Password Strength:", strength)
