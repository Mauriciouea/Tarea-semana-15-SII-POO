import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")
        
        # Lista interna para tareas (cada tarea es un string simple; usamos prefijo para estado)
        self.tareas = []
        
        # Campo de entrada
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda event: self.anadir_tarea())  # Enter para añadir
        
        # Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=5)
        
        btn_anadir = tk.Button(frame_botones, text="Añadir Tarea", command=self.anadir_tarea)
        btn_anadir.pack(side=tk.LEFT, padx=5)
        
        btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=self.marcar_completada)
        btn_completar.pack(side=tk.LEFT, padx=5)
        
        btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        btn_eliminar.pack(side=tk.LEFT, padx=5)
        
        # Listbox para mostrar tareas
        self.listbox = tk.Listbox(root, height=15, width=50)
        self.listbox.pack(pady=10)
        self.listbox.bind('<Double-1>', lambda event: self.marcar_completada())  # Doble clic para toggle completada
        
    def anadir_tarea(self):
        tarea = self.entry.get().strip()
        if tarea:
            self.tareas.append(tarea)  # Añadir a lista interna
            self.actualizar_listbox()
            self.entry.delete(0, tk.END)  # Limpiar entrada
        else:
            messagebox.showwarning("Advertencia", "Ingresa una tarea válida.")
    
    def marcar_completada(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            tarea_actual = self.tareas[indice]
            if tarea_actual.startswith("[✓] "):
                # Desmarcar: remover prefijo
                self.tareas[indice] = tarea_actual[4:]  # Quitar "[✓] "
            else:
                # Marcar: añadir prefijo
                self.tareas[indice] = "[✓] " + tarea_actual
            self.actualizar_listbox()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")
    
    def eliminar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_listbox()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")
    
    def actualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        for tarea in self.tareas:
            self.listbox.insert(tk.END, tarea)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
