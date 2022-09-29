# Aula 03 - exercício 01 - tuplas
import os
os.system('cls')

def qtd_par(vet):
    count = 0
    for v in vet:
        if v % 2 == 0:
            count += 1
    
    return count

def impares(vet):
    print("Ímpares: ", end='')
    for v in vet:
        if v % 2 == 1:
            print(v, end=' ')
    print()

def soma(vet):
    return sum(vet)

def maior(vet):
    return max(vet)

def menor(vet):
    return min(vet)

def positivos(vet):
    count = 0
    for v in vet:
        if v >= 0:
            count += 1
    return count

def main():
    vetor = (-2, 1, 4, -3, 7, 8)
    print(f"Quantidade de pares: {qtd_par(vetor)}")
    impares(vetor)
    print(f"Soma: {soma(vetor)}")
    print(f"Maior: {maior(vetor)}")
    print(f"Menor: {menor(vetor)}")
    print(f"Quantidade de positivos: {positivos(vetor)}")

main()