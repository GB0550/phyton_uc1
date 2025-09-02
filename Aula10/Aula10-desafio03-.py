import random 
matriz = []
for i in range(2): #linha
    linha = []
    for j in range(2): #coluna
        linha.append(random.randint(1, 1000))
    matriz.append(linha)
for linha in matriz:
    print(linha)
num = int(input("Digite o número para multiplicação: "))
resultado = matriz * num
print(f"A multiplicação é: ")

    #não finalizado