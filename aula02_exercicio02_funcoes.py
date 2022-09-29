# Aula 02 - exercício 02 - funções
import os
os.system('cls')

def html(nome, endereco, telefone, email, escola, exp_profissional):
    print("!DOCTYPE html")
    print("<html>")
    print(f"<head><title>Currículo {nome}</title></head>")
    print(f"""\t<body>
            <h3>Currículo de {nome}</h3>
            <p>Endereço: {endereco},
            <br>Telefone: {telefone},
            <br>Email: {email}</p>
            <p>Escolaridade: {escola}</p>
            <p>Experiência profissional: {exp_profissional}</p>
        </body>""")
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