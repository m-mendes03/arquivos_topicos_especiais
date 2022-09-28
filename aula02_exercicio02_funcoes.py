# Aula 02 - exercício 02 - funções
import os
os.system('cls')

def head(nome):
    print(f"<head><title>Currículo {nome}</title></head>")

def body(nome, endereco, telefone, email, escola, exp_pro):
    body = f"""\t<body>
            <h3>Currículo de {nome}</h3>
            <p>Endereço: {endereco},
            <br>Telefone: {telefone},
            <br>Email: {email}</p>
            <p>Escolaridade: {escola}</p>
            <p>Experiência profissional: {exp_pro}</p>
        </body>"""
    print(body)

def html(nome, endereco, telefone, email, escola, exp_profissional):
    print("!DOCTYPE html")
    print("<html>")
    head(nome)
    body(nome, endereco, telefone, email, escola, exp_profissional)
    print("</html>")

def main():
    nome = input("Digite o nome: ")
    endereco = input("Digite o endereço: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    escolaridade = input("Digite a escolaridade: ")
    experiencia_profissional = input("Digite a experiência profissional: ")
    html(nome, endereco, telefone, email, escolaridade, experiencia_profissional)

main()