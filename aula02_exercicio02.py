# Aula 02 - exercício 02
rn = []

for i in range(4):
    r = float(input(f"Digite o valor da resistência {i+1}: "))
    rn.append(r)

rn.sort()

re = 0
for r in rn:
    re += r

print(f"Resistência equivalente: {re}")
print(f"Menor resistência: {rn[0]}")
print(f"Maior resistência: {rn[len(rn)-1]}")