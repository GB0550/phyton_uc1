lista_pessoas= []
for i in range(2):
    pessoas={}
    pessoas["nome"]=input("Digite o nome: ")
    pessoas["idade"]=int(input("Digite a idade: "))
    pessoas["cidade"]=input("Digite a cidade: ")
    pessoas["email"]=input("Digite o email: ")
    lista_pessoas.append(pessoas)
print(lista_pessoas)