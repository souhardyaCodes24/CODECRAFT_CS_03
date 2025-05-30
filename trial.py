import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    feedback = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    print(f"\nPassword: {password}")
    print("Criteria Met:")
    print(f"✔️ \t Minimum Length (8+): {'Yes' if length_criteria else 'No'}")
    print(f"✔️ \t Uppercase Letter: {'Yes' if upper_criteria else 'No'}")
    print(f"✔️ \t Lowercase Letter: {'Yes' if lower_criteria else 'No'}")
    print(f"✔️ \t Digit: {'Yes' if digit_criteria else 'No'}")
    print(f"✔️ \t Special Character: {'Yes' if special_criteria else 'No'}\n")
    print(f"🛡️ \t Strength: {feedback[score]}")


# Example Usage

user_password = input("Enter a password to check: ")
check_password_strength(user_password)
