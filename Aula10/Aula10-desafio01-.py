import random 
matriz = []
for i in range(3): #linha
    linha = []
    for j in range(3): #coluna
        linha.append(random.randint(1, 1000))
    matriz.append(linha)
for linha in matriz:
    print(linha)