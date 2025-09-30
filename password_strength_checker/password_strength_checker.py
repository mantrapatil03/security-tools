# password_strength_checker.py

import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")

    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

    # Helpful tips
    if strength in ["Very Weak", "Weak"]:
        print("Tips to improve your password:")
        print("- Use at least 8 characters")
        print("- Include uppercase and lowercase letters")
        print("- Add digits (0-9)")
        print("- Add special characters (e.g., !, @, #, $)")

if __name__ == "__main__":
    main()




