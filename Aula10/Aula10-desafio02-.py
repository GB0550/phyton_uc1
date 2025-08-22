import random
matriz1 = [[random.randint(1, 30) for j in range(2)] for i in range(2)]
matriz2 = [[random.randint(1, 30) for j in range(2)] for i in range(2)]
soma = [[0, 0], [0, 0]]
for i in range(2):       
    for j in range(2):   
        soma[i][j] = matriz1[i][j] + matriz2[i][j]
print("Matriz 1:", matriz1)
print("Matriz 2:", matriz2)
print("Soma:", soma)