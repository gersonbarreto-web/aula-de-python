import os 
from dataclasses import dataclass
os.system("cls")

@dataclass
class pessoa :
    nome : str
    idade : int

    def mostrar_dados(self):
        print(f"nome: {self.nome}")
        print(f"idade:{self.idade}")


print("solicitando os dados da pessoa ")
pessoa1 = pessoa(nome=input("Digite seu nome : "),
                 idade=int(input("Digite sua idade:")))


pessoa2 = pessoa(nome=input("Digite seu nome : "),
                 idade=int(input("Digite sua idade:")))


print("\n= Exibindo dados =")
pessoa1.mostrar_dados()
print("\n= Exibindo dados da 2 pessoa =")
pessoa2.mostrar_dados()