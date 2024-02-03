import tkinter as tk
from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def calculate_button_clicked():
    birthdate_str = entry_birthdate.get()
    try:
        age = calculate_age(birthdate_str)
        result_label.config(text=f"You are {age} years old.")
    except ValueError:
        result_label.config(text="Invalid date format. Please use YYYY-MM-DD.")

# Create the main window
window = tk.Tk()
window.title("Age Calculator")

# Create widgets
label_birthdate = tk.Label(window, text="Enter your birthdate (YYYY-MM-DD):")
entry_birthdate = tk.Entry(window)
calculate_button = tk.Button(window, text="Calculate Age", command=calculate_button_clicked)
result_label = tk.Label(window, text="")

# Place widgets on the window
label_birthdate.pack(pady=10)
entry_birthdate.pack(pady=10)
calculate_button.pack(pady=10)
result_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
