import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.tasks = []

        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", width=12, command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=40, height=15, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", width=12, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Done", width=12, command=self.mark_done)
        self.complete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Task cannot be empty.")
        else:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
            del self.tasks[selected[0]]
        else:
            messagebox.showinfo("Info", "Select a task to delete.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            task = self.task_listbox.get(selected)
            self.task_listbox.delete(selected[0])
            self.task_listbox.insert(tk.END, f"✔️ {task}")
            self.tasks[selected[0]] = f"✔️ {task}"
        else:
            messagebox.showinfo("Info", "Select a task to mark as done.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
