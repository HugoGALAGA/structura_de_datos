import time
import string

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
clave_a_buscar_presente = 'A'  # Clave que sabemos que estará presente si llenamos con letras
clave_a_buscar_ausente = 'Z' # Clave que puede estar ausente o presente dependiendo del llenado y tamaño


# Instanciar y poblar las pilas con los tamaños respectivos y medir tiempos
for size in sizes:
    stack = Stack(size)

    # Medir tiempo de inserción (como en ejercicio 3)
    start_time_insertion = time.perf_counter()
    llenar_stack_con_letras(stack) # Usamos letras para llenar, puedes cambiar a `llenar_stack_con_ceros(stack)` si prefieres
    end_time_insertion = time.perf_counter()
    elapsed_time_insertion = end_time_insertion - start_time_insertion
    time_results_insertion.append((size, elapsed_time_insertion))
    instances.append(stack)
    print(f"Instancia con tamaño {size} creada y poblada en {elapsed_time_insertion:.6f} segundos.")

    # Medir tiempo de búsqueda (para clave presente)
    start_time_search_presente = time.perf_counter()
    stack.search(clave_a_buscar_presente)
    end_time_search_presente = time.perf_counter()
    elapsed_time_search_presente = end_time_search_presente - start_time_search_presente
    time_results_search.append((size, elapsed_time_search_presente))
    print(f"  Tiempo de búsqueda de '{clave_a_buscar_presente}' (presente) en tamaño {size}: {elapsed_time_search_presente:.6f} segundos.")

    # Medir tiempo de búsqueda (para clave ausente - opcional, pero informativo)
    start_time_search_ausente = time.perf_counter()
    stack.search(clave_a_buscar_ausente)
    end_time_search_ausente = time.perf_counter()
    elapsed_time_search_ausente = end_time_search_ausente - start_time_search_ausente
    print(f"  Tiempo de búsqueda de '{clave_a_buscar_ausente}' (ausente/presente) en tamaño {size}: {elapsed_time_search_ausente:.6f} segundos.") # Puede estar presente o no dependiendo del tamaño y letras

print("\nResumen de tiempos:")
print("Tiempos de inserción:")
for size, elapsed_time in time_results_insertion:
    print(f"Tamaño {size}: {elapsed_time:.6f} segundos")
print("\nTiempos de búsqueda (clave presente: '{clave_a_buscar_presente}'):")
for size, elapsed_time in time_results_search:
    print(f"Tamaño {size}: {elapsed_time:.6f} segundos")