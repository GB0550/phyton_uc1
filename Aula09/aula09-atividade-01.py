#exemplo de vetor 

vetor=[10, 20, 30, 40, 50]
print(f" Dados do vetor: {vetor}")

print(f" Dados da 4a posição: {vetor[3]}") 

for elemento in vetor :
    print(f"Vetor do elemento {elemento}")

for i in range (5) :
    print(f"{vetor[i]}")

for i in range (5) :
    print(f"O valor da {i+1}a posição é {vetor[i]}")


indice=1
for elemento in range(5) :
    print(f"O valor do indice {indice} é {elemento}")
    indice+=1
    
import random
numero = random.randint(1,187)
print(f"{numero}")

numeros = []
for i in range (20) :
    numeros.append(random.randint(1,187))

print(f"{numeros}")
soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)
qt_elementos = len(numeros)
media = soma/qt_elementos 
print(f"A soma dos elementos é: {soma}")
print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(f"A quantidade de elementos é: {qt_elementos}")
print(f"A media é: {media}")

#lista 2
numeros = []
for i in range (20) :
    numeros.append(random.randint(1, 100))

print(f"numero aleatorio gerado: {numeros}")

soma=sum(numeros)
maior=max(numeros)
menor=min(numeros)
qt_elementos=len(numeros)
media=soma/qt_elementos

print(f"\n\n\tSoma: {soma}, Maior: {maior}, Menor: {menor}, Quantidade de Elementos: {qt_elementos}, Média: {media}\n\n")



vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in vetor if num % 2 == 0]
impares = [num for num in vetor if num % 2 != 0]
print("Pares:", pares)
print("Ímpares:", impares)


produtos = (
    ("Arroz", 5.99),
    ("Feijão", 7.49),
    ("Leite", 4.89),
    ("Óleo", 9.99),
    ("Açúcar", 3.29)
)

print("LISTA DE PRODUTOS")
for nome, preco in produtos:
    print(f"{nome:.<20} R$ {preco:.2f}")


produtos = (
    ("Arroz", 5.99),
    ("Feijão", 7.49),
    ("Leite", 4.89),
    ("Óleo", 9.99),
    ("Açúcar", 3.29)
)

print("LISTA DE PRODUTOS")
total = 0

for nome, preco in produtos:
    quantidade = int(input(f"Quantidade de {nome}comprados: "))
    subtotal = preco * quantidade
    total += subtotal
    print(f"{nome:.<20} R$ {preco:.2f} x {quantidade} = R$ {subtotal:.2f}")

print(f"\nTOTAL A PAGAR: R$ {total:.2f}")