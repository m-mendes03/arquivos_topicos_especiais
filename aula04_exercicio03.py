palavra = input("Palavra para contar: ")

with open('dados/arquivo.txt', 'r') as arq:
    arq_read = arq.read()

palavra_count = arq_read.count(palavra)

print(palavra_count)