import random 
matriz_2 = []
for i in range(3): #linha
    linha = []
    for j in range(3): #coluna
        linha.append(random.randint(1, 1000))
    matriz_2.append(linha)
for linha in matriz_2:
    print(linha) 