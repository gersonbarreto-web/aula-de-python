import os
from dataclasses import dataclass
os.system ("cls")

@dataclass
class pessoa :
    nome : str
    email : str
    endereco : str

    def mostrar_dados(self):
        print(f"nome{self.nome}")
        print(f"email{self.email}")
        print(f"endereco{self.endereco}")


    def mostra_nome(self):
        print(f"nome{self.nome}")


print("solicitando dados ")
lista_pessoas = []

for i in range(2):
    pessoa =pessoa(nome=input("Digite seu nome: "),
                email=input("Digite seu email:"),
                endereco=input("Digite seu endereco:"))
lista_pessoas.append(pessoa)

print("\n Exibindo dados =")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()

print("\nSomente nome ")
for pessoa in lista_pessoas:
    pessoa.mostra_nome()




