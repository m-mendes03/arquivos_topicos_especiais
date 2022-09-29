with open('dados/arquivo.txt', 'r') as arq:
    with open('dados/arquivo_copia.txt', 'w') as arq_copia:
        arq_copia.write(arq.read())