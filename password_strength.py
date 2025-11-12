import re
import math

def calculate_password_strength(password):
    # Score initialization
    score = 0
    feedback = []

    # Length check
    length = len(password)
    if length < 6:
        feedback.append("Password is too short (min 6 chars recommended).")
    elif length < 10:
        score += 0.5
        feedback.append("Try using at least 10 characters.")
    else:
        score += 1

    # Uppercase, lowercase, digits, symbols
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")
        
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
        
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include some numbers.")
        
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Use a special character like @ or #.")
        
    # Avoid common passwords
    common_passwords = ["password", "123456", "admin", "qwerty", "letmein", "welcome"]
    if password.lower() in common_passwords:
        score -= 2
        feedback.append("Avoid using common passwords.")
        
    # Calculate entropy (approx)
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[@$!%*?&]", password): charset += 10
    entropy = math.log2(charset ** len(password)) if charset > 0 else 0

    # Normalize final score
    strength = min(score / 5, 1)
    return strength, feedback, round(entropy, 2)

# For quick testing
if __name__ == "__main__":
    pwd = input("Enter a password: ")
    strength, feedback, entropy = calculate_password_strength(pwd)
    print(f"\nPassword Score: {round(strength, 2)}")
    print(f"Entropy: {entropy} bits")
    if strength < 0.4:
        print("Strength: Weak 🔴")
    elif strength < 0.8:
        print("Strength: Moderate 🟡")
    else:
        print("Strength: Strong 🟢")

    print("\nSuggestions:")
    for tip in feedback:
        print(f"- {tip}")
