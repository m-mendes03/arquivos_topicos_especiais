import os
from unicodedata import normalize
import random
os.system('cls')

lista_nomes = []
op = True
while op:
    nome = input('Insira o nome: ')

    #username = nome[0].lower() + nome.lower().split(' ').pop()
    username = normalize('NFKD', nome[0].lower() + nome.lower().split(' ').pop()).encode('ascii', 'ignore').decode('ascii')
    i = 1
    for usr in lista_nomes:
        if usr['username'] == username:
            username += str(i)
            i += 1

    senha = ''
    for i in range(8):
        rand = random.randint(0, 126)
        senha = senha + chr(rand)

    user = {
        "nome": nome,
        "username": username,
        "senha": senha
    }

    lista_nomes.append(user)

    ch = input('Continuar? S/N ').upper()
    if ch[0] == 'N':
        op = False

listaNomes = sorted(lista_nomes, key= lambda x: x['username'])

for usr in listaNomes:
    print(usr)