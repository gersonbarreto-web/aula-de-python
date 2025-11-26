import os 
os. system("cls|| clear")


#crod usando a lista
#crate criar salva
#read solicitar busca
#update atualizar ou notifica
#delete deletar ou excluir 



lista_cliente = []

#crate 
print("create - adicionar / inserir")
nome = input("Digite seu nome")
lista_cliente.append(nome)
print(f"o nome: {nome} foi inserido com sucesso ! ")

"red"
print("\nread - ler / Mostrar")
print(lista_cliente)

#update
print("\nUpdate - Atualizar / Alterar")
nome_para_atualizar = "nome"
if nome_para_atualizar in lista_cliente:
    novo_nome = "nome"
    indice = lista_cliente.index(nome_para_atualizar)
    lista_cliente[indice] = novo_nome
    print(f" o nome {nome_para_atualizar} foi atualizadp para {novo_nome}.")
else :
    print(f" o nome {nome_para_atualizar} nao foi encontrado")

print(lista_cliente)

print("\ndelete excluir / remover")
nome_para_excluir = input("Digite um nome para excluir")
if nome_para_atualizar in lista_cliente:
    lista_cliente.remove(nome_para_atualizar)
    print (f"{"nome_para_excluir"} foi excluindo com sucesso")
else : 
    print(f"o nome {nome_para_excluir} nao foi encontrado")
   
input("...")