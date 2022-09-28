# Aula 02 - exercício 02
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = round((peso/(altura**2)), 2)

if(imc < 18.59):
    print(f"IMC: {imc}\nAbaixo do peso.")
elif(imc >= 18.60 and imc < 24.99):
    print(f"IMC: {imc}\nPeso ideal.")
elif(imc >= 25.00 and imc < 29.99):
    print(f"IMC: {imc}\nSobrepeso.")
elif(imc >= 30.00):
    print(f"IMC: {imc}\nObesidade.")