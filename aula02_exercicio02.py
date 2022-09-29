# Aula 02 - exercício 02
rn = []

for i in range(4):
    r = float(input(f"Digite o valor da resistência {i+1}: "))
    rn.append(r)

print(f"Resistência equivalente: {sum(rn)}")
print(f"Menor resistência: {min(rn)}")
print(f"Maior resistência: {max(rn)}")