import tkinter as tk
import random
import string

def generate_password():
    user_name = name_entry.get()
    password_length = int(length_entry.get())
    
    if password_length <= 0:
        result_label.config(text="Invalid password length")
        return

    password_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(password_characters) for i in range(password_length))
    
    result_label.config(text=f"Generated password for {user_name}: {generated_password}")

root = tk.Tk()
root.title("Password Generator")
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()
length_label = tk.Label(root, text="Enter password length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()
result_label = tk.Label(root, text="", height=8, width=50, wraplength=500)
result_label.pack()

root.mainloop()
