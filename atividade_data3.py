import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Funcionario :
    nome : str
    data_ad : str
    matricula : str
    endereco : str
    def exibir_dados(self):
        print(f"nome:{self.nome}\ndata_ad:{self.data_ad}\nmatricula:{self.matricula}\nendereco:{self.endereco}")

@dataclass
class Cliente :
    nome : str 
    data_n : str
    endereco : str
    def exibir_dados1(self):
        print(f"nome:{self.nome}\ndata_n:{self.data_n}\nendereco{self.endereco}")

lista_de_funcionario = []
QUANTIDADE_DE_FUNCIONARIO = 3

for i in range (QUANTIDADE_DE_FUNCIONARIO):
    funcionario = Funcionario(
        nome = input ("Digite seu nome : "),
        data_ad = input ("Digite sua data de admissao : "),
        matricula = input ("Digite sua matricula : "),
        endereco = input(" Digite seu endereco"),
    )

    lista_de_funcionario.append(funcionario)
    print()


lista_de_cliente = []
QUANTIDADE_DE_CLIENTE = 3

for i in range (QUANTIDADE_DE_CLIENTE):
    cliente = Cliente(
        nome = input ("Digite seu nome : "),
        data_n = input ("Digite sua data de nascimento : "),
        endereco = input ("Digite seu endereco : "),
    )

    lista_de_cliente.append(cliente)
    print()

nome_do_arquivo = "dados_fucionario.csv"
with open(nome_do_arquivo, "a") as arquivo_funcionario :
    for funcionario in lista_de_funcionario :
        arquivo_funcionario.write(f"nome_f :{funcionario.nome}\n data_ad : {funcionario.data_ad}\n matricula : {funcionario.matricula}\n endereco : {funcionario.endereco}\n")

    print("Dados salvos com sucesso. ")

nome_da_pasta = "dados_cliente.csv"
with open(nome_da_pasta,  "a") as arquivo_cliente :
    for cliente in lista_de_cliente :
        arquivo_cliente.write(f"nome_cl : {cliente.nome}\n data_n : {cliente.data_n}\n endereco :{cliente.endereco}\n")
    print ("Dados salvo com sucesso. ")



