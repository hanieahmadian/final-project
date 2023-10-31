import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox.delete(0, tk.END)


root = tk.Tk()
root.title("To-Do List")


listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=20)


entry = tk.Entry(root, width=30)
entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=5)


root.mainloop()