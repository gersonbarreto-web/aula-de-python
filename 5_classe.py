import os 
from dataclasses import dataclass
os.system("cls")

@dataclass
class pessoa :
    nome : str
    email : str
    endereco : str

    def dados_entrega(self):
        print(f"nome:{self.nome}")
        print(f"endereco:{self.endereco}")

    def dados_email(self):
        print(f"nome:{self.nome} ")
        print(f"email:{self.email}")        
        
print("solicitando dados do email")
pessoa1 = pessoa (nome=input("Digite seu nome :"),
                  email=input("Digiete seu email "),
                  endereco=input("Digite seu endreco"))              

print("\n= Exibindo dados ")
pessoa1.dados_entrega()
pessoa1.dados_email()
