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
        
        # Configuración de la interfaz gráfica
        self.root = root
        self.root.title("Simulación de Navegador")
        
        self.label = tk.Label(root, text=f"Página actual: {self.page_names[self.peek]}", font=("Arial", 16))
        self.label.pack(pady=10)
        
        self.btn_siguiente = tk.Button(root, text="→", font=("Arial", 14), command=self.siguiente)
        self.btn_siguiente.pack(side=tk.RIGHT, padx=10)
        
        self.btn_anterior = tk.Button(root, text="←", font=("Arial", 14), command=self.anterior)
        self.btn_anterior.pack(side=tk.LEFT, padx=10)
        
        self.btn_cargar = tk.Button(root, text="C", font=("Arial", 14), command=self.cargar)
        self.btn_cargar.pack(side=tk.TOP, pady=10)
        
        self.btn_salir = tk.Button(root, text="E", font=("Arial", 14), command=self.salir)
        self.btn_salir.pack(side=tk.BOTTOM, pady=10)

    def actualizar_label(self):
        self.label.config(text=f"Página actual: {self.page_names[self.peek]}")

    def cargar(self):
        self.actualizar_label()

    def siguiente(self):
        if len(self.queue2) >= self.max_size:
            self.label.config(text="Usted ya está en la última ventana que visitó.")
            return
        
        self.queue2.append(self.peek)
        if self.queue1:
            self.peek = self.queue1.pop()
        self.actualizar_label()

    def anterior(self):
        if len(self.queue1) >= self.max_size:
            self.label.config(text="Usted ya está en la primera ventana que abrió.")
            return
        
        self.queue1.append(self.peek)
        if self.queue2:
            self.peek = self.queue2.pop()
        self.actualizar_label()
    
    def salir(self):
        self.label.config(text="Gracias por usar Mell Browser")
        self.root.update()
        time.sleep(3)
        self.root.quit()

# Iniciar la aplicación gráfica
root = tk.Tk()
browser = BrowserSimulation(root)
root.mainloop()