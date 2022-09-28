# Aula 02 - exercício 04
ano = int(input("Digite o ano: "))

if(ano % 100 == 0):
    seculo = (ano // 100)
elif(ano % 100 != 0):
    seculo = (ano // 100) + 1

print(f"The century from the year {ano} is {seculo}.")