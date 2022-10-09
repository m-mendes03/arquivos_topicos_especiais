## PROVA TÓPICOS ESPECIAIS - EXERCÍCIO 05

import os
import json
from datetime import datetime

os.system('cls')

def menu():
    print('Varejo do João')
    print('[1] Cadastrar produtos')
    print('[2] Relatório de produtos')
    print('[3] Relatório de estoque baixo')
    print('[4] Exportar dados')
    print('[0] Sair')

def cadastrar_produto(nome_produto, valor_compra, qtd_estoque, prods):
    codigo = 1
    if len(prods) > 0:
        codigo = max(map(lambda x: x['codigo'], prods)) + 1
    valor_venda = valor_compra * 1.25
    produto = {
            "codigo": codigo,
            "nome_do_produto": nome_produto,
            "valor_da_compra": valor_compra,
            "valor_venda": valor_venda,
            "quantidade_em_estoque": qtd_estoque
        }
    return produto

def relatorio_produto(produtos):
    prod = sorted(produtos, key= lambda x: x['nome_do_produto'])
    for p in prod:
        print(p)

def relatorio_estoque_baixo(produtos):
    for p in produtos:
        if p['quantidade_em_estoque'] <= 5:
            print(p)

def exportar_dados(produtos):
    data = datetime.now().strftime('%Y%m%d%H%M%S')
    fp = 'dados/relatorios/relatorio_' + data + '.json'
    with open(fp, 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)

def main():
    produtos = []
    op = True
    while(op):
        menu()
        try:
            esc = int(input("Digite o número do menu: "))
            if esc == 0:
                print('Bye!')
                op = False
                break
            elif esc == 1:
                nome_produto = input("Digite o nome do produto: ")
                valor_compra = float(input("Digite o valor da compra: "))
                qtd_estoque = int(input("Digite a quantidade em estoque: "))
                produtos.append(cadastrar_produto(nome_produto, valor_compra, qtd_estoque, produtos))
            elif esc == 2:
                relatorio_produto(produtos)
            elif esc == 3:
                relatorio_estoque_baixo(produtos)
            elif esc == 4:
                exportar_dados(produtos)
            else:
                print('Opção inválida')
        except ValueError:
            print('Valor incorreto digitado!')

main()