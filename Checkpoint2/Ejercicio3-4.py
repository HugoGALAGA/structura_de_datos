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

def llenar_stack_con_letras(stack): # Función para llenar con letras (usando letras del abecedario como en ejercicio 3)
    letters = string.ascii_uppercase
    for i in range(stack.capacity):
        stack.push(letters[i % len(letters)])

def llenar_stack_con_ceros(stack): # Función para llenar con ceros (como en la imagen de ejemplo)
    for i in range(stack.capacity):
        stack.push(0)

# Determinar los tamaños de las estructuras (usando el 'n' encontrado en ejercicio 2 - ASUME que n=22000000 es el valor encontrado)
n = 22000000  # **REEMPLAZA ESTE VALOR con el 'n' que encontraste en el ejercicio 2**
sizes = [n, 2*n, 3*n, 4*n, 5*n]
instances = []
time_results_insertion = []
time_results_search = []
memory_results_creation = []
memory_results_population = []
memory_results_search = []
clave_a_buscar_presente = 'A'  # Clave que sabemos que estará presente si llenamos con letras
clave_a_buscar_ausente = 'Z' # Clave que puede estar ausente o presente dependiendo del llenado y tamaño


# Instanciar y poblar las pilas con los tamaños respectivos y medir tiempos y memoria
for size in sizes:
    # Medir memoria antes de la creación de la instancia
    mem_before_creation = memory_usage()[0]

    stack = Stack(size)

    # Medir memoria después de la creación de la instancia
    mem_after_creation = memory_usage()[0]
    memory_results_creation.append((size, mem_after_creation - mem_before_creation))
    print(f"Instancia con tamaño {size} creada. Memoria usada en creación: {memory_results_creation[-1][1]:.2f} MB.")


    # Medir tiempo de inserción (como en ejercicio 3)
    start_time_insertion = time.perf_counter()
    llenar_stack_con_letras(stack) # Usamos letras para llenar, puedes cambiar a `llenar_stack_con_ceros(stack)` si prefieres
    end_time_insertion = time.perf_counter()
    elapsed_time_insertion = end_time_insertion - start_time_insertion
    time_results_insertion.append((size, elapsed_time_insertion))

    # Medir memoria después de poblar la instancia
    mem_after_population = memory_usage()[0]
    memory_results_population.append((size, mem_after_population - mem_after_creation)) # Diferencia desde la creación
    print(f"Instancia con tamaño {size} poblada en {elapsed_time_insertion:.6f} segundos. Memoria usada en población: {memory_results_population[-1][1]:.2f} MB.")


    instances.append(stack)


    # Medir tiempo de búsqueda (para clave presente)
    start_time_search_presente = time.perf_counter()
    stack.search(clave_a_buscar_presente)
    end_time_search_presente = time.perf_counter()
    elapsed_time_search_presente = end_time_search_presente - start_time_search_presente
    time_results_search.append((size, elapsed_time_search_presente))
    print(f"  Tiempo de búsqueda de '{clave_a_buscar_presente}' (presente) en tamaño {size}: {elapsed_time_search_presente:.6f} segundos.")

    # Medir memoria después de búsqueda (clave presente) - Opcional, para ver si la búsqueda afecta la memoria
    mem_after_search = memory_usage()[0]
    memory_results_search.append((size, mem_after_search - mem_after_population)) # Diferencia desde la población
    print(f"  Memoria usada en búsqueda de '{clave_a_buscar_presente}' (presente) en tamaño {size}: {memory_results_search[-1][1]:.2f} MB.")


    # Medir tiempo de búsqueda (para clave ausente - opcional, pero informativo)
    start_time_search_ausente = time.perf_counter()
    stack.search(clave_a_buscar_ausente)
    end_time_search_ausente = time.perf_counter()
    elapsed_time_search_ausente = end_time_search_ausente - start_time_search_ausente
    print(f"  Tiempo de búsqueda de '{clave_a_buscar_ausente}' (ausente/presente) en tamaño {size}: {elapsed_time_search_ausente:.6f} segundos.") # Puede estar presente o no dependiendo del tamaño y letras
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