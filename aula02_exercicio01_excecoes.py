# Aula 02 - exercício 01 - exceções
import os
os.system('cls')

op = True
while op:
    try:
        peso = float(input("Digite o peso: "))
        altura = float(input("Digite a altura: "))
        print(f"O IMC é {round(peso/(altura**2),2)}")
    except ValueError:
        print("Valor inválido.")
    ch = input("Deseja continuar? (s/n) ")
    if ch[0].upper() == 'N':
        op = False