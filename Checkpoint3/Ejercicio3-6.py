import time
import string
import matplotlib.pyplot as plt

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_full(self):
        return len(self.stack) >= self.capacity

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.stack.pop()

    def search(self, key):
        try:
            return self.stack.index(key)
        except ValueError:
            return -1

    def __str__(self):
        return " -> ".join(map(str, self.stack))

def llenar_stack_con_letras(stack):
    letters = string.ascii_uppercase
    for i in range(stack.capacity):
        stack.push(letters[i % len(letters)])

# Determinar los tamaños de las estructuras (usando el 'n' encontrado en ejercicio 2)
n = 22000000  # Reemplaza con el 'n' real si es diferente

sizes = [n, 2*n, 3*n, 4*n, 5*n]
instances = []
time_results_insertion = []
time_results_search = []
clave_a_buscar_presente = 'A'

# Instanciar y poblar las pilas y medir tiempos (solo insercion y busqueda)
for size in sizes:
    stack = Stack(size)

    # Medir tiempo de inserción
    start_time_insertion = time.perf_counter()
    llenar_stack_con_letras(stack)
    end_time_insertion = time.perf_counter()
    elapsed_time_insertion = end_time_insertion - start_time_insertion
    time_results_insertion.append((size, elapsed_time_insertion))
    instances.append(stack)
    print(f"Instancia con tamaño {size} creada y poblada en {elapsed_time_insertion:.6f} segundos.")

    # Medir tiempo de búsqueda
    start_time_search = time.perf_counter()
    stack.search(clave_a_buscar_presente)
    end_time_search = time.perf_counter()
    elapsed_time_search = end_time_search - start_time_search
    time_results_search.append((size, elapsed_time_search))
    print(f"  Tiempo de búsqueda de '{clave_a_buscar_presente}' en tamaño {size}: {elapsed_time_search:.6f} segundos.")


# --- Crear la gráfica ---
stack_sizes = [size for size, _ in time_results_insertion] # tamaños del eje x
search_times = [time for _, time in time_results_search] # tiempos de busqueda eje y
delete_times = [0] * len(stack_sizes) # tiempos de delete en 0, ya que no se midieron

plt.figure(figsize=(10, 6)) # tamaño de la figura

plt.plot(stack_sizes, search_times, marker='o', linestyle='-', color='blue', label='Search') # Grafica de Search
plt.plot(stack_sizes, delete_times, marker='s', linestyle='--', color='red', label='Delete') # Grafica de Delete (en 0)

plt.xlabel('Tamaño de la Instancia (en millones)', fontsize=12) # Eje X label
plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12) # Eje Y label
plt.title('Tiempos de Search y Delete vs Tamaño de la Pila', fontsize=14) # Titulo del grafico
plt.grid(True) # Muestra la grilla
plt.legend() # Muestra la leyenda

# Formatear el eje X para mostrar tamaños en millones
def millions_formatter(x, pos):
    return f'{x / 1000000:.1f}M'
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(millions_formatter))

plt.savefig('search_delete_tiempos_pila.png') # Guarda la grafica como PNG
plt.show() # Muestra la grafica (opcional)

print("\nGráfica 'search_delete_tiempos_pila.png' creada y guardada.")