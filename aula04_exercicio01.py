n = int(input("Número de linhas para ser lido: "))

with open('dados/arquivo.txt', 'r') as arq:
    for i in range(n):
        print(arq.readline(), end='')