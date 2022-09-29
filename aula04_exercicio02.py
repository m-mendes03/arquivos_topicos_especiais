arq_read=[]
with open('dados/arquivo.txt', 'r') as arq:
    arq_read = arq.readlines()
for l in arq_read:
    print(l, end='')