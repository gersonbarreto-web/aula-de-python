import os
import time
from dataclasses import dataclass

os.system("cls || clear")  # limpa o terminal em windows ou linux

lista_funcionarios = []

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    cpf: str
    funcao: str

    def mostra_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"CPF: {self.cpf}")
        print(f"Função: {self.funcao}")


# função para verificar se a lista está vazia
def lista_esta_vazia(lista_func):
    if not lista_func:
        print("\nNão há funcionários cadastrados.")
        return True
    return False


# função para adicionar funcionário
def adicionar_funcionario(lista_func):
    print("\n--- Adicionar novo funcionário ---")
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF: ")
    funcao = input("Digite a função do funcionário: ")

    novo_funcionario = Funcionario(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        funcao=funcao
    )

    lista_func.append(novo_funcionario)

    print(f"\nFuncionário {nome} adicionado com sucesso!")


# função para encontrar funcionário
def encontra_funcionario_por_nome(lista_funcionarios, nome_buscar):
    nome_buscar = nome_buscar.lower()
    for funcionario in lista_funcionarios:
        if funcionario.nome.lower() == nome_buscar:
            return funcionario
    return None


# mostrar todos os funcionários
def mostra_todos_funcionarios(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return

    print("\n--- Lista de Funcionários ---")
    for funcionario in lista_funcionarios:
        funcionario.mostra_dados()


# atualizar funcionário
def atualizar_funcionarios(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return

    mostra_todos_funcionarios(lista_funcionarios)

    print("\n--- Atualizar Funcionário ---")
    nome_buscar = input("\nDigite o nome do funcionário: ")

    funcionario = encontra_funcionario_por_nome(lista_funcionarios, nome_buscar)

    if funcionario:
        print("\nFuncionário encontrado.")
        print("\nDeixe em branco para manter o valor atual.\n")

        print(f"Nome atual: {funcionario.nome}")
        novo_nome = input("Novo nome: ")

        print(f"Data de nascimento atual: {funcionario.data_nascimento}")
        nova_data = input("Nova data de nascimento: ")

        print(f"CPF atual: {funcionario.cpf}")
        novo_cpf = input("Novo CPF: ")

        print(f"Função atual: {funcionario.funcao}")
        nova_funcao = input("Nova função: ")

        if novo_nome:
            funcionario.nome = novo_nome
        if nova_data:
            funcionario.data_nascimento = nova_data
        if novo_cpf:
            funcionario.cpf = novo_cpf
        if nova_funcao:
            funcionario.funcao = nova_funcao

        print("\nFuncionário atualizado com sucesso!")
    else:
        print("\nFuncionário não encontrado.")


# excluir funcionário
def excluir_funcionario(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return

    mostra_todos_funcionarios(lista_funcionarios)

    print("\n--- Excluir Funcionário ---")
    nome_buscar = input("\nDigite o nome do funcionário: ")

    funcionario = encontra_funcionario_por_nome(lista_funcionarios, nome_buscar)

    if funcionario:
        lista_funcionarios.remove(funcionario)
        print("\nFuncionário removido com sucesso!")
    else:
        print("\nFuncionário não encontrado.")


# MENU PRINCIPAL
while True:
    print("""
--- Gerenciador de Funcionários ---
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
            adicionar_funcionario(lista_funcionarios)
        case 2:
            mostra_todos_funcionarios(lista_funcionarios)
        case 3:
            atualizar_funcionarios(lista_funcionarios)
        case 4:
            excluir_funcionario(lista_funcionarios)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida! Tente novamente.")

    time.sleep(3)
    os.system("cls || clear")