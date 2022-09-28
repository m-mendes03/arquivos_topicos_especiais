# Aula 02 - exercício 01 - funções
import os
os.system('cls')

def is_par(num):
    return num % 2 == 0

def quantidade_par(par):
    return len(par)

def show_impar(impar):
    print("Ímpares:")
    for i in impar:
        print(i, end=', ')

def ordena_lista(lis):
    return lis.sort()

def menor_num(lis):
    return lis[0]

def maior_num(lis):
    return lis[len(lis)-1]

def media(lis):
    soma = 0
    for l in lis:
        soma += l
    return soma/len(lis)

def main():
    op = True
    par = []
    impar = []
    lista = []
    while op:
        try:
            num = int(input("Digite um inteiro: "))
            if is_par(num):
                par.append(num)
            else:
                impar.append(num)
            lista.append(num)
            ch = input("Deseja continuar? (s/n) ")
            if ch[0].upper() == 'N':
                op = False
        except ValueError:
            print("Entrada inválida.")
    ordena_lista(lista)
    print(f"Quantidade de pares: {len(par)}")
    print(f"Quantidade de impares: {len(impar)}")
    show_impar(impar)
    print(f"O maior número é: {maior_num(lista)}")
    print(f"O menor número é: {menor_num(lista)}")
    print(f"A média é: {media(lista)}")

main()