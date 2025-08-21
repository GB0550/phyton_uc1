# Criando uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9,]
]
print("Elemento (0,0):", matriz[0][0])  # Saída: 1
print("Elemento (2,1):", matriz[2][1])  # Saída: 8
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()


#codigo 2

import random
matriz_1 = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = random.randint(0, 100)
        linha.append(elemento)
    matriz_1.append(linha)

for linha in matriz_1:
    print(linha)

#codigo 3

import random
matriz_2 = []
for i in range(3):
    linha=[]

    for j in range (3):
        #linha.append(i)
        #linha.append(j)
        #linha.append(rrandom.randint(0.100))
        valor=random.randint(0,100)
        linha.append(valor)

        matriz_2.append(linha)

        print (f"{matriz_2}")

#codigo 4

for linha in matriz_2 :
    print(f"{linha}")


#codigo 5

for linha in matriz_2 :
    for valor in linha :
        print(f"{linha}")

#codigo 6
for linha in matriz_2 :
    for valor in linha :
        print(f"{valor}", end=" ")
#codigo 
"""   
matriz_2 = []
for i in range(3): #linha
    linha = []
    for j in range(3): #coluna
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz_2.append(linha)

for linha in matriz_2:
    print(linha) 
"""
