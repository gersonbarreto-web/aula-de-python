import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class pacientes :
    nome : str
    idade : int 
    peso : str
    cpf : str
    altura : str
    def exibir_dados(self):
        print(f"nome:{self.nome}\nidade: {self.idade}")
        
lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range (QUANTIDADE_DE_PACIENTES):
    pacientes = pacientes(
        nome = input ("Digite seu nome : "),
        idade = int(input("Digite sua idade")),
       
    )
    
    lista_de_pacientes.append(pacientes)
    print() # pular uma linha 
    
nome_do_arquivo = "dados_pacientes.csv"
with open(nome_do_arquivo, "a") as arquivo_pacientes :
    for pacientes in lista_de_pacientes :
        arquivo_pacientes.write(f"{pacientes.nome},{pacientes.idade}")
    print("Dados salvos com sucesso.")

#print("\nExibindo lista de pacientes :")
#for pacientes in lista_de_pacientes:
 #   pacientes.exibir_dados()            
 
    #"r" - reand - leitura 
print("\nExibindo todos os pacientes :")
lista = []
try:
    # "r" - read - leitura
    with open(nome_do_arquivo, "r", encoding="uft-8") as arquivo :
        # recebe todos os dados do arquivo de uma so vez
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes :
            nome, idade = pacientes.strip().split(",")
            dados_paciente = pacientes(nome=nome, idade=int(idade))
            lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados()                    
except FileNotFoundError:
    print("o arquivo nao foi encontrado.")    