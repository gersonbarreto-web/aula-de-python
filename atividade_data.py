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

print("\n Exibindo dados dos funcionarios : ")
lista = []
try : 
    with open(nome_do_arquivo, "r", encoding="uft-8") as arquivo :
        lista_de_funcionario = arquivo.readlines()
        for funcionario in lista_de_funcionario :
            nome,data_ad,matricula,endereco = funcionario.strip().split(",")
            dados_funcionario =  nome, data_ad, matricula, endereco = funcionario (nome=nome, data_ad=data_ad,matricula=matricula,endereco=endereco)
            lista.append(dados_funcionario)
    for funcionario in lista : 
        funcionario.exibir_dados()
except FileNotFoundError :
    print("o arquivo nao foi encotrado.")

def mostra_fucionario(lista):
    print("\n=== LISTA DE FUNCIONARIOS ===")
    for f in lista :
        print(f"nome:{f["nome"]}")
        print(f"data de amdissao : {f["data_ad"]}")
        print(F"matricula : {f["matricula"]}")
        print(f"endereco: {f[endereco]}")

print("\n Exibindo dados dos clientes : ")
lista1 = []
try :
    with open (nome_da_pasta, "r", encoding="uft-8") as pasta :
        lista_de_cliente = pasta.readlines()
        for cliente in lista_de_cliente :
            nome , data_n ,endereco = cliente.strip().split(",")
            dados_cliente = nome,data_n,endereco = cliente (nome=nome,data_n=data_n,endereco=endereco)
            lista1.append(dados_cliente)
    for cliente in lista1 :
        cliente.exibir_dados()
except FileNotFoundError : 
    print("arquivo nao encontrado")

def mostra_cliente(lista1) :
    print("\n=== LISTA DE CLIENTE ===")
    for f in lista1 :
        print(f"nome: {f["nome"]}")
        print(f"data de nascimento : {f[data_n]}")
        print(f"endereco : {f[endereco]}")   
def main():
    funcionarios = ler_csv("funcionarios.csv")
    clientes = ler_csv("clientes.csv")

    mostrar_funcionario(funcionarios)
    mostrar_cliente(clientes)


