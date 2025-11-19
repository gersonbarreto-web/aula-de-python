import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class pacientes :
    nome : str
    data : str
    RG : str
    cpf : str
    def exibir_dados(self):
        print(f"nome:{self.nome}\nidade: {self.data}\nRG:{self.RG}\ncpf:{self.cpf}")
lista_de_pacientes = [] 
QUANDTIDADE_DE_PACIENTES = 5

for i in range (QUANDTIDADE_DE_PACIENTES):
    pacientes = pacientes(
        nome = input ("Digite seu nome : "),
        data = input("Digite sua data de nascimento"),
        RG = input ("Digite seu RG : "),
        cpf = input ("Digite seu cpf : "),
    )       
    
    lista_de_pacientes.append(pacientes)
    print()
    
nome_do_arquivo = "dados_pacientes.csv"
with open(nome_do_arquivo, "a") as arquivo_pacientes :
    for  pacientes in lista_de_pacientes :
        arquivo_pacientes.write(f"{pacientes.nome},{pacientes.data},{pacientes.RG},{pacientes.cpf}")
    print("Dados salvos com sucesso.") 
    
print("\nExibindo todos os pacientes :")
lista = []
try:
    with open(nome_do_arquivo,"r", encoding="uft-8") as arquivo :
       lista_todos_pacientes = arquivo.readlines()
       for pacientes in lista_todos_pacientes :
           nome,data ,RG , cpf = pacientes.strip().split(",")
           nome,data,RG,cpf,=pacientes(nome=nome,data=data,RG=RG,cpf=cpf)
           lista.append(dados_pacientes)
    for pacientes in lista:
        pacientes.exibir_dados()
except FileNotFoundError:
    print("o arquivo nao foi encontrado")                     
        