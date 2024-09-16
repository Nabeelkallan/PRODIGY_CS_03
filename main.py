import re

def assess_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        strength += 1

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if strength == 4:
        feedback.append("Password is strong.")
    elif strength == 3:
        feedback.append("Password is medium strength.")
    else:
        feedback.append("Password is weak.")

    return feedback

password = input("Enter your password: ")
result = assess_password_strength(password)
for message in result:
    print(message)
