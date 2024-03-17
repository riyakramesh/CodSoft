import tkinter as tk

def add_to_display(value):
    current = display_var.get()
    if current == "Error":
        display_var.set(value)
    else:
        display_var.set(current + value)

def clear_display():
    display_var.set("")

def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception:
        display_var.set("Error")

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception:
        display_var.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

display_var = tk.StringVar()
display_var.set("")

display = tk.Entry(root, textvariable=display_var, font=('Arial', 14), bd=10, insertwidth=4, width=25, justify='right')
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, font=('Arial', 14), padx=20, pady=20, command=clear_display)
    elif text == '=':
        button = tk.Button(root, text=text, font=('Arial', 14), padx=20, pady=20, command=calculate)
    else:
        button = tk.Button(root, text=text, font=('Arial', 14), padx=20, pady=20, command=lambda value=text: add_to_display(value))
    button.grid(row=row, column=col)

root.mainloop()