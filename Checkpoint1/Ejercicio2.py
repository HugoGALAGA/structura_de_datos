import time

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

# Medir el tiempo de inserción en la pila
n = 24000000
stack = Stack(n)
start_time = time.perf_counter()

for i in range(n):
    stack.push(i)

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Tiempo de inserción para n={n}: {elapsed_time:.6f} segundos")
