import os 
from dataclasses import dataclass
os.system("cls")

@dataclass
class pessoa:
    nome: str
    email: str
    telefone: str
    endereco: str

print("solicitando os dados da pessoa")
pessoa1= pessoa(nome=input("Digite seu nome "),
                email=input("Digite seu email"),
                telefone=input("Digite seu telefone"),
                endereco=input("Digite seu indereco"))

print(f"nome{pessoa1.nome}\nemail:{pessoa1.email}\ntelefone{pessoa1.telefone}\nendereco{pessoa1.endereco}")