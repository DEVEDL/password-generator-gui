import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_entry.get()
    
    if not length.isdigit():
        messagebox.showerror("Error", "Enter a valid number")
        return
    
    length = int(length)
    
    if length < 4:
        messagebox.showerror("Error", "Minimum length is 4")
        return

    chars = "abcdefghijklmnopqrstuvwxyz"

    if upper_var.get():
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if digit_var.get():
        chars += "0123456789"
    if symbol_var.get():
        chars += "!@#$%^&*()"

    password = "".join(random.choice(chars) for _ in range(length))
    
    result_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

upper_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digit_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).pack()

tk.Button(root, text="Copy", command=copy_password).pack(pady=5)

root.mainloop()