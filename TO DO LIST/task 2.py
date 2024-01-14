import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

root = tk.Tk()
root.title("To Do")
entry = tk.Entry(root, width=60)
entry.pack(pady=30)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=30)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=30)

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=80)

root.mainloop()
