import time
import string
from memory_profiler import memory_usage

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

def llenar_stack_con_ceros(stack):
    for i in range(stack.capacity):
        stack.push(0)

n = 22000000  
sizes = [n, 2*n, 3*n, 4*n, 5*n]
instances = []
time_results_insertion = []
time_results_search = []
memory_results_creation = []
memory_results_population = []
memory_results_search = []
clave_a_buscar_presente = 'A'  
clave_a_buscar_ausente = 'Z' 


for size in sizes:
    mem_before_creation = memory_usage()[0]

    stack = Stack(size)

    mem_after_creation = memory_usage()[0]
    memory_results_creation.append((size, mem_after_creation - mem_before_creation))
    print(f"Instancia con tamaño {size} creada. Memoria usada en creación: {memory_results_creation[-1][1]:.2f} MB.")


    start_time_insertion = time.perf_counter()
    llenar_stack_con_letras(stack) 
    end_time_insertion = time.perf_counter()
    elapsed_time_insertion = end_time_insertion - start_time_insertion
    time_results_insertion.append((size, elapsed_time_insertion))

    mem_after_population = memory_usage()[0]
    memory_results_population.append((size, mem_after_population - mem_after_creation)) # Diferencia desde la creación
    print(f"Instancia con tamaño {size} poblada en {elapsed_time_insertion:.6f} segundos. Memoria usada en población: {memory_results_population[-1][1]:.2f} MB.")


    instances.append(stack)


    start_time_search_presente = time.perf_counter()
    stack.search(clave_a_buscar_presente)
    end_time_search_presente = time.perf_counter()
    elapsed_time_search_presente = end_time_search_presente - start_time_search_presente
    time_results_search.append((size, elapsed_time_search_presente))
    print(f"  Tiempo de búsqueda de '{clave_a_buscar_presente}' (presente) en tamaño {size}: {elapsed_time_search_presente:.6f} segundos.")

    mem_after_search = memory_usage()[0]
    memory_results_search.append((size, mem_after_search - mem_after_population)) 
    print(f"  Memoria usada en búsqueda de '{clave_a_buscar_presente}' (presente) en tamaño {size}: {memory_results_search[-1][1]:.2f} MB.")


    start_time_search_ausente = time.perf_counter()
    stack.search(clave_a_buscar_ausente)
    end_time_search_ausente = time.perf_counter()
    elapsed_time_search_ausente = end_time_search_ausente - start_time_search_ausente
    print(f"  Tiempo de búsqueda de '{clave_a_buscar_ausente}' (ausente/presente) en tamaño {size}: {elapsed_time_search_ausente:.6f} segundos.")
    print("-" * 50)


print("\nResumen de tiempos:")
print("Tiempos de inserción:")
for size, elapsed_time in time_results_insertion:
    print(f"Tamaño {size}: {elapsed_time:.6f} segundos")
print("\nTiempos de búsqueda (clave presente: '{clave_a_buscar_presente}'):")
for size, elapsed_time in time_results_search:
    print(f"Tamaño {size}: {elapsed_time:.6f} segundos")

print("\nResumen de memoria (MB):")
print("Memoria usada en creación de instancia:")
for size, mem_usage in memory_results_creation:
    print(f"Tamaño {size}: {mem_usage:.2f} MB")
print("\nMemoria usada en población de instancia:")
for size, mem_usage in memory_results_population:
    print(f"Tamaño {size}: {mem_usage:.2f} MB")
print("\nMemoria usada en búsqueda de clave presente:")
for size, mem_usage in memory_results_search:
    print(f"Tamaño {size}: {mem_usage:.2f} MB")
