import os 
from dataclasses import dataclass
os.system("cls")


@dataclass
class cliente:
    nome: str
    idade: int
    peso : float
    altura:float


    def mostra_dados_cliente(self):
        print(f"\nNome :{self.nome}")
        print(f"idade:{self.idade}")
        print(f"peso : {self.peso}")
        print(f"altura :{self.altura}")


lista_de_clientes =[]

for i in range(4):
    dados_cliente=cliente(nome=input("Digite seu nome "),
                          idade=int(input("Digite sua idade")),
                          peso=float(input("Digite seu peso ")),
                          altura=float(input("Digite sua altura ")))
    lista_de_clientes.append(dados_cliente)
    os.system("cls")

for cliente in lista_de_clientes:
    cliente.mostra_dados_cliente()

