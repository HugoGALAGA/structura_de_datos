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

n = 22000000  

sizes = [n, 2*n, 3*n, 4*n, 5*n]
instances = []
time_results_insertion = []
time_results_search = []
clave_a_buscar_presente = 'A'

for size in sizes:
    stack = Stack(size)

    start_time_insertion = time.perf_counter()
    llenar_stack_con_letras(stack)
    end_time_insertion = time.perf_counter()
    elapsed_time_insertion = end_time_insertion - start_time_insertion
    time_results_insertion.append((size, elapsed_time_insertion))
    instances.append(stack)
    print(f"Instancia con tamaño {size} creada y poblada en {elapsed_time_insertion:.6f} segundos.")

    start_time_search = time.perf_counter()
    stack.search(clave_a_buscar_presente)
    end_time_search = time.perf_counter()
    elapsed_time_search = end_time_search - start_time_search
    time_results_search.append((size, elapsed_time_search))
    print(f"  Tiempo de búsqueda de '{clave_a_buscar_presente}' en tamaño {size}: {elapsed_time_search:.6f} segundos.")


# --- Crear la gráfica ---
stack_sizes = [size for size, _ in time_results_insertion] 
search_times = [time for _, time in time_results_search] 
delete_times = [0] * len(stack_sizes) 

plt.figure(figsize=(10, 6)) 

plt.plot(stack_sizes, search_times, marker='o', linestyle='-', color='blue', label='Search')
plt.plot(stack_sizes, delete_times, marker='s', linestyle='--', color='red', label='Delete') 

plt.xlabel('Tamaño de la Instancia (en millones)', fontsize=12) 
plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12) 
plt.title('Tiempos de Search y Delete vs Tamaño de la Pila', fontsize=14) 
plt.grid(True) 
plt.legend() 

def millions_formatter(x, pos):
    return f'{x / 1000000:.1f}M'
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(millions_formatter))

plt.savefig('search_delete_tiempos_pila.png') 
plt.show() 

print("\nGráfica 'search_delete_tiempos_pila.png' creada y guardada.")
