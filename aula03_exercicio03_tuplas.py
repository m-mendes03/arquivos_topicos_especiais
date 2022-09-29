# Aula 03 - exercício 03 - tuplas
import os
import collections
os.system('cls')

Aluno = collections.namedtuple('Aluno', 'nome nota1 nota2 media situacao')

alunos = []
try:
        for i in range(6):
                nome = input("Nome: ")
                nota1 = float(input("Nota prova 1: "))
                nota2 = float(input("Nota prova 2: "))
                media = (nota1 + nota2)/ 2
                if media >= 6.0:
                        situacao = 'aprovado'
                elif media < 6:
                        situacao = 'reprovado'
                alunos.append(Aluno(nome, nota1, nota2, media, situacao))
        avg = 0
        aprovados = 0
        reprovados = 0
        for a in alunos:
                avg += a.media
                if a.situacao == 'aprovado':
                        aprovados += 1
                else:
                        reprovados += 1
        avg /= len(alunos)

        print(f"Média da classe: {round(avg, 2)}")
        print(f"Aprovados: {round(aprovados*100/len(alunos),2)}%")
        print(f"Reprovados: {round(reprovados*100/len(alunos), 2)}%")
except ValueError:
        print('Nota inválida.')