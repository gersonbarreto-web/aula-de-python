import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class cliente:
    nome : str
    endereco : Endereco

cliente1 = cliente (nome="marta", 
            endereco=Endereco(
                logradouro="Rua A",
                numero=23))

print("mostra dados do cliente.")
print(f"nome: {cliente1.nome}")
print(f"Endereco:{cliente1.endereco.logradouro}")
print(f"numero:{cliente1.endereco.numero}")