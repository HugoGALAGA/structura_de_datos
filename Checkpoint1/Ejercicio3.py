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

# Determinar los tamaños de las estructuras
n = 2400000
sizes = [n, 2*n, 3*n, 4*n, 5*n]
instances = []

def get_letter(index):
    letters = string.ascii_uppercase
    return letters[index % len(letters)]

time_results = []

# Instanciar y poblar las pilas con los tamaños respectivos
for size in sizes:
    stack = Stack(size)
    start_time = time.perf_counter()
    for i in range(size):
        stack.push(get_letter(i))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    time_results.append((size, elapsed_time))
    instances.append(stack)
    print(f"Instancia con tamaño {size} creada y poblada en {elapsed_time:.6f} segundos.")

print("Todas las estructuras han sido creadas y pobladas.")
print("Tiempos de inserción:")
for size, elapsed_time in time_results:
    print(f"Tamaño {size}: {elapsed_time:.6f} segundos")
