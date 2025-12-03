import os
import time
from dataclasses import dataclass

os.system("cls || clear")  # limpa o terminal em windows ou linux

lista_alunos = []

@dataclass
class Aluno:
    nome: str
    data_nascimento: str
    ra: str
    curso: str
    logradouro: str
    numero: str
    cidade: str
    estado: str

    def mostra_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"RA: {self.ra}")
        print(f"Curso: {self.curso}")
        print(f"Logradouro: {self.logradouro}")
        print(f"Número: {self.numero}")
        print(f"Cidade: {self.cidade}")
        print(f"Estado: {self.estado}")


# função para verificar se a lista está vazia
def lista_esta_vazia(lista_alunos):
    if not lista_alunos:
        print("\nNão há alunos cadastrados.")
        return True
    return False


# função para adicionar aluno
def adicionar_aluno(lista_alunos):
    print("\n--- Adicionar novo aluno ---")
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    ra = input("Digite o RA: ")
    curso = input("Digite o curso: ")
    
    print("\n--- Endereço do Aluno ---")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    novo_aluno = Aluno(
        nome=nome,
        data_nascimento=data_nascimento,
        ra=ra,
        curso=curso,
        logradouro=logradouro,
        numero=numero,
        cidade=cidade,
        estado=estado
    )

    lista_alunos.append(novo_aluno)

    print(f"\nAluno {nome} adicionado com sucesso!")


# função para encontrar aluno por nome
def encontra_aluno_por_nome(lista_alunos, nome_buscar):
    nome_buscar = nome_buscar.lower()
    for aluno in lista_alunos:
        if aluno.nome.lower() == nome_buscar:
            return aluno
    return None


# mostrar todos os alunos
def mostra_todos_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    print("\n--- Lista de Alunos ---")
    for aluno in lista_alunos:
        aluno.mostra_dados()


# atualizar aluno
def atualizar_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    mostra_todos_alunos(lista_alunos)

    print("\n--- Atualizar Aluno ---")
    nome_buscar = input("\nDigite o nome do aluno: ")

    aluno = encontra_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno:
        print("\nAluno encontrado.")
        print("\nDeixe em branco para manter o valor atual.\n")

        print(f"Nome atual: {aluno.nome}")
        novo_nome = input("Novo nome: ")

        print(f"Data de nascimento atual: {aluno.data_nascimento}")
        nova_data = input("Nova data de nascimento: ")

        print(f"RA atual: {aluno.ra}")
        novo_ra = input("Novo RA: ")

        print(f"Curso atual: {aluno.curso}")
        novo_curso = input("Novo curso: ")

        print(f"Logradouro atual: {aluno.logradouro}")
        novo_logradouro = input("Novo logradouro: ")

        print(f"Número atual: {aluno.numero}")
        novo_numero = input("Novo número: ")

        print(f"Cidade atual: {aluno.cidade}")
        nova_cidade = input("Nova cidade: ")

        print(f"Estado atual: {aluno.estado}")
        novo_estado = input("Novo estado: ")

        if novo_nome:
            aluno.nome = novo_nome
        if nova_data:
            aluno.data_nascimento = nova_data
        if novo_ra:
            aluno.ra = novo_ra
        if novo_curso:
            aluno.curso = novo_curso
        if novo_logradouro:
            aluno.logradouro = novo_logradouro
        if novo_numero:
            aluno.numero = novo_numero
        if nova_cidade:
            aluno.cidade = nova_cidade
        if novo_estado:
            aluno.estado = novo_estado

        print("\nAluno atualizado com sucesso!")
    else:
        print("\nAluno não encontrado.")


# excluir aluno
def excluir_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    mostra_todos_alunos(lista_alunos)

    print("\n--- Excluir Aluno ---")
    nome_buscar = input("\nDigite o nome do aluno: ")

    aluno = encontra_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno:
        lista_alunos.remove(aluno)
        print("\nAluno removido com sucesso!")
    else:
        print("\nAluno não encontrado.")


# MENU PRINCIPAL
while True:
    print("""
--- Gerenciador de Alunos ---
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
            adicionar_aluno(lista_alunos)
        case 2:
            mostra_todos_alunos(lista_alunos)
        case 3:
            atualizar_alunos(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida! Tente novamente.")

    time.sleep(3)
    os.system("cls || clear")