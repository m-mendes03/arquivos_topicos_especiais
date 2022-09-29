# Aula 03 - exercício 02 - tuplas
import os
import random
os.system('cls')

mat = [[random.randint(0, 255) for i in range(10)] for j in range(10)]

for m in mat:
    print(m)