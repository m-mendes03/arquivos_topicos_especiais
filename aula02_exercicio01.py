# Aula 02 - exercício 01


nome_produto = input(f"Digite o nome do produto: ")

is_positivo = True
while(is_positivo):
    valor_produto = float(input(f"Digite o valor do produto: "))
    if(valor_produto <= 0):
        print(f"Valor do produto inválido.")
        continue
    is_positivo = False
    
if(valor_produto < 50.00):
    valor_desconto = valor_produto
elif(valor_produto >= 50.00 and valor_produto < 200.00):
    valor_desconto = round((valor_produto * 0.95), 2)
elif(valor_produto >= 200.00 and valor_produto < 500.00):
    valor_desconto = round((valor_produto * 0.94), 2)
elif(valor_produto >= 500.00 and valor_produto < 1000.00):
    valor_desconto = round((valor_produto * 0.93), 2)
elif(valor_produto >= 1000.00):
    valor_desconto = round((valor_produto * 0.92), 2)

print(f"Produto: {nome_produto}")
print(f"Valor: {valor_produto}")
print(f"Valor com desconto: {valor_desconto}")