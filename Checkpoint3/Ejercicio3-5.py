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

def llenar_stack_con_letras(stack):
    letters = string.ascii_uppercase
    for i in range(stack.capacity):
        stack.push(letters[i % len(letters)])

# Determinar los tamaños de las estructuras (usando el 'n' encontrado previamente)
n = 22000000 # REEMPLAZA ESTE VALOR CON TU 'n' REAL
sizes = [n, 2*n, 3*n, 4*n, 5*n]
instances = []

# Crear y poblar las instancias (esto se hace solo una vez al inicio)
print("Creando y poblando las instancias de Stack...")
for size in sizes:
    stack = Stack(size)
    llenar_stack_con_letras(stack) # Poblar cada stack
    instances.append(stack)
print("Instancias creadas y pobladas.\n")

def ejecutar_busqueda_inexistente(instance_index):
    stack_instance = instances[instance_index - 1] # Ajuste de índice (1-5 a 0-4)
    size = sizes[instance_index - 1]
    clave_inexistente = '#' # Probablemente no esté en el abecedario
    start_time_search_inexistente = time.perf_counter()
    stack_instance.search(clave_inexistente) # Perform the linear search
    end_time_search_inexistente = time.perf_counter()
    elapsed_time_search_inexistente = end_time_search_inexistente - start_time_search_inexistente
    instrucciones_search = 1 #  One call to search, representing a full linear scan
    print(f"Tiempo de búsqueda LINEAL (elemento inexistente) en Stack {instance_index} (tamaño {size}): {elapsed_time_search_inexistente:.6f} segundos. Instancias search (lineal scan): {instrucciones_search}")
    return size, elapsed_time_search_inexistente, instrucciones_search

def ejecutar_pop(instance_index):
    stack_instance = instances[instance_index - 1] # Ajuste de índice (1-5 a 0-4)
    size = sizes[instance_index - 1]
    start_time_pop_total = time.perf_counter()
    pop_count = 0
    while not stack_instance.is_empty(): # Vaciar el stack completo
        stack_instance.pop()
        pop_count += 1
    end_time_pop_total = time.perf_counter()
    elapsed_time_pop_total = end_time_pop_total - start_time_pop_total
    instrucciones_pop = pop_count # Number of pop operations to empty the stack
    print(f"Tiempo para VACiar Stack {instance_index} (tamaño {size}) usando pop: {elapsed_time_pop_total:.6f} segundos. Instancias pop (para vaciar): {instrucciones_pop}")
    return size, elapsed_time_pop_total, instrucciones_pop

resultados_perfilamiento_busqueda_inexistente = []
resultados_perfilamiento_pop = []

while True:
    print("\nElija una operación para perfilar:")
    print("a - Búsqueda LINEAL de elemento inexistente (recorrer todo el stack)")
    print("b - Vaciar el Stack completo usando pop")
    print("c - Salir")
    opcion_principal = input("Opción (a/b/c): ").lower()

    if opcion_principal == 'a':
        while True:
            print("\nElija la instancia de Stack para búsqueda inexistente (1-5):")
            print("1 - n")
            print("2 - 2n")
            print("3 - 3n")
            print("4 - 4n")
            print("5 - 5n")
            print("v - Volver al menú principal")
            opcion_instancia_a = input("Opción (1-5/v): ").lower()
            if opcion_instancia_a in ['1', '2', '3', '4', '5']:
                size_search, tiempo_search, instrucciones_search = ejecutar_busqueda_inexistente(int(opcion_instancia_a))
                resultados_perfilamiento_busqueda_inexistente.append({'operacion': 'busqueda_lineal_inexistente', 'tamaño': size_search, 'tiempo': tiempo_search, 'instancias': instrucciones_search})
            elif opcion_instancia_a == 'v':
                break
            else:
                print("Opción inválida.")

    elif opcion_principal == 'b':
        while True:
            print("\nElija la instancia de Stack para operación vaciar con pop (1-5):")
            print("1 - n")
            print("2 - 2n")
            print("3 - 3n")
            print("4 - 4n")
            print("5 - 5n")
            print("v - Volver al menú principal")
            opcion_instancia_b = input("Opción (1-5/v): ").lower()
            if opcion_instancia_b in ['1', '2', '3', '4', '5']:
                size_pop, tiempo_pop, instrucciones_pop = ejecutar_pop(int(opcion_instancia_b))
                resultados_perfilamiento_pop.append({'operacion': 'vaciar_con_pop', 'tamaño': size_pop, 'tiempo': tiempo_pop, 'instancias': instrucciones_pop})
            elif opcion_instancia_b == 'v':
                break
            else:
                print("Opción inválida.")

    elif opcion_principal == 'c':
        break

    else:
        print("Opción inválida.")

print("\nResultados del perfilamiento:")
print("\nBúsqueda LINEAL de elemento inexistente (recorrido completo):")
for resultado in resultados_perfilamiento_busqueda_inexistente:
    print(f"Tamaño: {resultado['tamaño']}, Tiempo: {resultado['tiempo']:.6f} segundos, Instancias search (lineal scan): {resultado['instancias']}")

print("\nVaciar Stack completo usando pop:")
for resultado in resultados_perfilamiento_pop:
    print(f"Tamaño: {resultado['tamaño']}, Tiempo: {resultado['tiempo']:.6f} segundos, Instancias pop (para vaciar): {resultado['instancias']}")

print("\nPrograma finalizado.")