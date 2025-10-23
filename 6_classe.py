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
pessoa1 =pessoa(nome=input("Digite seu nome: "),
                email=input("Digite seu email:"),
                endereco=input("Digite seu endereco:"))


pessoa2 =pessoa(nome=input("Digite seu nome : "),
                email=input("Digite seu email :"),
                endereco=input("Digite seu endereco :"))

print("\n Exibindo dados =")
pessoa1.mostrar_dados()
pessoa1.mostra_nome()

pessoa2.mostrar_dados()
pessoa2.mostra_nome()

