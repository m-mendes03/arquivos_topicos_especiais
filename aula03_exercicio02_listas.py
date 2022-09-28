# Aula 03 - exercício 02 - listas
import os
import random
os.system('cls')

vetor = []
for i in range(15):
        vetor.append(random.randint(-256, 256))

vetor.sort()

print(vetor)

vetor = list(map(lambda x: round(x/vetor[len(vetor)-1], 2), vetor))

print(vetor)
