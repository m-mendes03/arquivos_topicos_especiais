## PROVA TÓPICOS ESPECIAIS - EXERCÍCIO 03

import datetime
import os

os.system('cls')

hoje = datetime.datetime.now()

print(f'Data atual: {str(hoje.date())}')
print(f'Ano atual: {hoje.year}')
print(f'Mês atual: {hoje.month}')
print(f'Dia atual: {hoje.day}')
print(f'Data (dia/mês/ano): {hoje.strftime("%d/%m/%Y")}')
print(f'Data (dia de mês_por_extenso de ano): {hoje.strftime("%d de %B de %Y")}')