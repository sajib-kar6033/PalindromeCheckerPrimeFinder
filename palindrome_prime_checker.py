import tkinter as tk
from tkinter import messagebox

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_number():
    try:
        number = int(entry.get())
        palindrome_result = is_palindrome(number)
        prime_result = is_prime(number)

        result_message = f"Number: {number}\n"
        result_message += f"Palindrome: {'Yes' if palindrome_result else 'No'}\n"
        result_message += f"Prime: {'Yes' if prime_result else 'No'}"

        messagebox.showinfo("Result", result_message)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Palindrome Checker and Prime Number Finder")

# Create and place the input label and entry
label = tk.Label(root, text="Enter a number:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# Create and place the check button
check_button = tk.Button(root, text="Check", command=check_number)
check_button.pack(pady=20)

# Run the application
root.mainloop()
