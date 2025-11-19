import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}")

lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: "))
    )
    lista_de_pacientes.append(paciente)
    print() # Pular uma linha.

nome_do_arquivo = "dados_pacientes.csv"
with open(nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")
    print("Dados salvos com sucesso.")

print("\nExibindo todos os pacientes: ")
try:
    # "r" - read - leitura
    with open(nome_do_arquivo, "r") as arquivo:
        # Recebe todos os dados do arquivo de uma só vez.
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            print(f"- {paciente.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")