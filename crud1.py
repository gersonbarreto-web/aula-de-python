import os
import time
from dataclasses import dataclass

os.system("cls || clear")  # limpa o terminal em windows ou linux

lista_clientes = []

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostra_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")


# função para verificar se a lista está vazia
def lista_esta_vazia(lista_cliente):
    if not lista_cliente:
        print("\nNão há clientes cadastrados.")
        return True
    return False


# função para adicionar cliente
def adicionar_cliente(lista_cliente):
    print("\n--- Adicionar novo cliente ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_cliente.append(novo_cliente)

    print(f"\nCliente {nome} adicionado com sucesso!")


# função para encontrar cliente
def encontra_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar:
            return cliente
    return None


# mostrar todos os clientes
def mostra_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return

    print("\n--- Lista de Clientes ---")
    for cliente in lista_clientes:
        cliente.mostra_dados()


# atualizar cliente
def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return

    mostra_todos_clientes(lista_clientes)

    print("\n--- Atualizar Cliente ---")
    nome_buscar = input("\nDigite o nome do cliente: ")

    cliente_para_atualizar = encontra_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar:
        print("\nCliente encontrado.")
        print("\nDeixe em branco para manter o valor atual.\n")

        print(f"Nome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"E-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo email: ")

        print(f"Telefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone

        print("\nCliente atualizado com sucesso!")
    else:
        print("\nCliente não encontrado.")


# excluir cliente
def excluir_cliente(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return

    mostra_todos_clientes(lista_clientes)

    print("\n--- Excluir Cliente ---")
    nome_buscar = input("\nDigite o nome do cliente: ")

    cliente = encontra_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente:
        lista_clientes.remove(cliente)
        print("\nCliente removido com sucesso!")
    else:
        print("\nCliente não encontrado.")


# MENU PRINCIPAL
while True:
    print("""
--- Gerenciador de Clientes ---
1 - Adicionar
2 - Mostrar todos
3 - Atualizar
4 - Excluir
0 - Sair
    """)

    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("\nEntrada inválida! Digite um número.")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_cliente(lista_clientes)
        case 2:
            mostra_todos_clientes(lista_clientes)
        case 3:
            atualizar_clientes(lista_clientes)
        case 4:
            excluir_cliente(lista_clientes)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida! Tente novamente.")

    time.sleep(3)
    os.system("cls || clear")