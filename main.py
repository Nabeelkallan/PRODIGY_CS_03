import re


def assess_password_strength(password):
    strength = 0
    feedback = []

    # Criteria 1: Length of password
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        strength += 1

    # Criteria 2: Uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    # Criteria 3: Numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Criteria 4: Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Provide feedback based on strength
    if strength == 4:
        feedback.append("Password is strong.")
    elif strength == 3:
        feedback.append("Password is medium strength.")
    else:
        feedback.append("Password is weak.")

    return feedback


# Example usage
password = input("Enter your password: ")
result = assess_password_strength(password)
for message in result:
    print(message)
