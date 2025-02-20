from collections import deque
import tkinter as tk
import time

class BrowserSimulation:
    def __init__(self, root):
        self.queue1 = deque(['a', 'b', 'c'])
        self.queue2 = deque(['d', 'e', 'f'])
        self.peek = 'z'
        self.max_size = 6  # Máximo de elementos en cada cola
        self.page_names = {
            'a': 'Carros', 'b': 'Animales', 'c': 'Peluches',
            'd': 'Anime', 'e': 'Manga', 'f': 'Computadoras', 'z': 'Miu'
        }
        self.history = ['Miu']  # Historial de navegación
        
        # Configuración de la interfaz gráfica
        self.root = root
        self.root.title("Simulación de Navegador")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")
        
        self.label = tk.Label(root, text=f"Página actual: {self.page_names[self.peek]}", font=("Arial", 16), bg="#f0f0f0")
        self.label.pack(pady=10)
        
        self.history_label = tk.Label(root, text="Historial:", font=("Arial", 12), bg="#f0f0f0")
        self.history_label.pack(pady=5)
        
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        self.btn_anterior = tk.Button(button_frame, text="←", font=("Arial", 14), command=self.anterior, width=5, bg="#d9d9d9")
        self.btn_anterior.grid(row=0, column=0, padx=5)
        
        self.btn_siguiente = tk.Button(button_frame, text="→", font=("Arial", 14), command=self.siguiente, width=5, bg="#d9d9d9")
        self.btn_siguiente.grid(row=0, column=1, padx=5)
        
        self.btn_historial = tk.Button(button_frame, text="H", font=("Arial", 14), command=self.mostrar_historial, width=5, bg="#d9d9d9")
        self.btn_historial.grid(row=1, column=0, padx=5, pady=5)
        
        self.btn_limpiar_historial = tk.Button(button_frame, text="LH", font=("Arial", 14), command=self.limpiar_historial, width=5, bg="#ff9999")
        self.btn_limpiar_historial.grid(row=1, column=1, padx=5, pady=5)
        
        self.btn_salir = tk.Button(root, text="E", font=("Arial", 14), command=self.salir, width=10, bg="#ff6666")
        self.btn_salir.pack(pady=10)

        # Vincular teclas
        self.root.bind('<Left>', lambda event: self.anterior())
        self.root.bind('<Right>', lambda event: self.siguiente())
        self.root.bind('h', lambda event: self.mostrar_historial())
        self.root.bind('e', lambda event: self.salir())
        self.root.bind('l', lambda event: self.limpiar_historial())

    def actualizar_label(self):
        self.label.config(text=f"Página actual: {self.page_names[self.peek]}")

    def mostrar_historial(self):
        historial_texto = "Historial: " + " -> ".join(self.history)
        self.history_label.config(text=historial_texto)
    
    def limpiar_historial(self):
        self.history = [self.page_names[self.peek]]
        self.history_label.config(text="Historial:")
    
    def siguiente(self):
        if len(self.queue2) >= self.max_size:
            self.label.config(text="Usted ya está en la última ventana que visitó.")
            return
        
        self.queue2.append(self.peek)
        if self.queue1:
            self.peek = self.queue1.pop()
            self.history.append(self.page_names[self.peek])
        self.actualizar_label()

    def anterior(self):
        if len(self.queue1) >= self.max_size:
            self.label.config(text="Usted ya está en la primera ventana que abrió.")
            return
        
        self.queue1.append(self.peek)
        if self.queue2:
            self.peek = self.queue2.pop()
            self.history.append(self.page_names[self.peek])
        self.actualizar_label()
    
    def salir(self):
        self.label.config(text="Gracias por usar Mell Browser")
        self.root.update()
        self.root.after(3000, self.root.quit)

# Iniciar la aplicación gráfica
root = tk.Tk()
browser = BrowserSimulation(root)
root.mainloop()
