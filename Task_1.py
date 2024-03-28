import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

tasks = []

root = tk.Tk()
root.title("My To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()