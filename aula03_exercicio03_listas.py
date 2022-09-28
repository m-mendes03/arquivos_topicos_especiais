# Aula 03 - exercício 03 - listas
import os
import random
os.system('cls')

arr = []
for i in range(6):
        arr.append(random.randint(-10, 10))

print(arr)

n = len(arr) - 1
prod = 0
for a in range(0, n):
        if prod < arr[a] * arr[a+1]:
                prod = arr[a] * arr[a+1]
                i = arr[a]
                j = arr[a+1]
        
print(f"Produto: {prod}  ({i} * {j})")