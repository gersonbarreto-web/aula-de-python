import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class cliente:
    nome : str
    cpf : str
    telefone : str

    def mostra_dados(self):
        print(f"\nnome: {self.nome}")
        print(f"cpf:{self.cpf}")
        print(f"telefone:{self.telefone}\n")

    def dados_sms(self):
        print(f"telefone:{self.telefone}")

print("solicitando dados ") 
pessoa1 = cliente (nome=input("digite seu nome "),
                   cpf=input("digite seu cpf"),
                   telefone=input("digite seu telefone "))


print("\n= Exibindo dados ")
pessoa1.mostra_dados()
print("\n Exibindo dados sms")
pessoa1.dados_sms()