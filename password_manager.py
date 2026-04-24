import tkinter as tk
from tkinter import messagebox
import json
import random
import string
import os

FILE_NAME = "passwords.json"

# Load data
def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Generate password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Add password
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showerror("Error", "All fields required!")
        return

    data = load_data()
    data[website] = {"username": username, "password": password}
    save_data(data)

    messagebox.showinfo("Saved", "Password saved successfully!")

    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Search password
def search_password():
    website = website_entry.get()
    data = load_data()

    if website in data:
        info = data[website]
        messagebox.showinfo("Details",
            f"Username: {info['username']}\nPassword: {info['password']}")
    else:
        messagebox.showerror("Not Found", "No data found!")

# UI
root = tk.Tk()
root.title("🔐 Password Manager")
root.geometry("400x350")

tk.Label(root, text="Password Manager", font=("Arial",16,"bold")).pack(pady=10)

# Website
website_entry = tk.Entry(root, width=30)
website_entry.pack(pady=5)
website_entry.insert(0, "Website")

# Username
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)
username_entry.insert(0, "Username")

# Password
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)
password_entry.insert(0, "Password")

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
tk.Button(root, text="Save", command=add_password).pack(pady=5)
tk.Button(root, text="Search", command=search_password).pack(pady=5)

root.mainloop()