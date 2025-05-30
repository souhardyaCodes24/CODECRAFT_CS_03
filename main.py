import tkinter as tk
from tkinter import messagebox
import re



def startapp():
    # Function to evaluate password strength
    def check_password_strength():
        password = entry.get()

        # Criteria
        length_criteria = len(password) >= 8
        upper_criteria = re.search(r'[A-Z]', password) is not None
        lower_criteria = re.search(r'[a-z]', password) is not None
        digit_criteria = re.search(r'\d', password) is not None
        special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

        # Score and feedback
        score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
        feedback = {
            5: "Very Strong",
            4: "Strong",
            3: "Moderate",
            2: "Weak",
            1: "Very Weak",
            0: "Extremely Weak"
        }

        # Update labels
        result_label.config(text=f"\nPassword Strength: {feedback[score]}")
        criteria_label.config(text=(
            f"✔ Length ≥ 8: {'✅' if length_criteria else '❌'}\n"
            f"✔ Uppercase Letter: {'✅' if upper_criteria else '❌'}\n"
            f"✔ Lowercase Letter: {'✅' if lower_criteria else '❌'}\n"
            f"✔ Digit: {'✅' if digit_criteria else '❌'}\n"
            f"✔ Special Char: {'✅' if special_criteria else '❌'}"
        ))


    
    
    
    # GUI setup
    root = tk.Tk()
    root.title("Password Complexity Checker")
    root.geometry("600x400")
    root.resizable(False, False)

    def reload():
        
        root.destroy()
        startapp()
  


    tk.Label(root, text="Enter Password:", font=('Arial', 12)).pack(pady=10)
    entry = tk.Entry(root, width=30,  font=('Arial', 12))
    entry.pack(pady=5)

    tk.Button(root, text="Check Strength", command=check_password_strength, font=('Arial', 12)).pack(pady=10)

    tk.Button(root, text="Reload", command=reload, font=('Arial', 12)).pack(pady=10,padx=10)

    result_label = tk.Label(root, text="", font=('Arial', 12, 'bold'))
    result_label.pack(pady=5)

    criteria_label = tk.Label(root, text="", font=('Arial', 10), justify='left')
    criteria_label.pack(pady=5)

    label = tk.Label(root, text="By: Souhardya", font=('Arial', 10), justify='right')
    label.pack(pady=10)

    root.mainloop()

startapp()