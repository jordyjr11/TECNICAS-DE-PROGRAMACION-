import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, StringVar

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        self.tasks = []  # Lista para almacenar tareas

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Botones
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.mark_completed_button = tk.Button(root, text="Marcar Completada", command=self.mark_completed)
        self.mark_completed_button.pack(pady=5)

        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Lista para mostrar tareas
        self.task_listbox = Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Scrollbar
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Asociar atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("c", lambda event: self.mark_completed())
        self.root.bind("d", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def mark_completed(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            completed_task_text = f"{task} (Completada)"
            self.tasks[selected_index] = completed_task_text
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para marcarla como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminarla.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()