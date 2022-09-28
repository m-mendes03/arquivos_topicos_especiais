# Aula 03 - exercício 04 - tuplas
import os
import collections
os.system('cls')

Produto = collections.namedtuple('Produto', 'nome preco')

produtos = []

for i in range(5):
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        produtos.append(Produto(nome, preco))

qtd = 0
media = 0
nomes = []
for p in produtos:
        if p.preco < 50.0:
                qtd += 1
        elif 50.00 <= p.preco <= 100.00:
                nomes.append(p.nome)
        elif p.preco > 100.00:
                media += p.preco
media /= len(produtos)

print(f"Quantidade com preço inferior a $50.00: {qtd}")
print(f"Nome dos produtos com preço entre $50.00 e $100.00: {nomes}")
print(f"Média dos preços superiores a $100.00: {media}")
