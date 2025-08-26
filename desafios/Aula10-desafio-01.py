#gerando as matrizes
import random
matriz1 = [[random.randint(1, 999) for j in range(10)] for i in range(10)]
matriz2 = [[random.randint(1, 999) for j in range(10)] for i in range(10)]
#gerando a soma
soma = [[0 for j in range(10)] for i in range(10)]

for i in range(10):       
    for j in range(10):   
        soma[i][j] = matriz1[i][j] + matriz2[i][j]

print("Matriz 1:")
for linha in matriz1:
    print(linha)

print("\nMatriz 2:")
for linha in matriz2:
    print(linha)

print("\nSoma:")
for linha in soma:
    print(linha)
    total = 0
elementos = 10 * 10  # total de elementos da matriz
for i in range(10):
    for j in range(10):
        total += soma[i][j]
media = total / elementos
print(f"\nMédia: {media:.2f}")