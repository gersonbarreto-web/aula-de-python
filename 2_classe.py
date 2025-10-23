import os 
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso : float
    altura: float

print("solicitando os dados da pessoa")
pessoa1=Pessoa (nome=input("Digite seu nome: "),
               idade=int(input("Digite sua idade:")),
               peso=float(input("Digite seu peso")),
               altura=float(input("Digite sua altura")))


print(f"nome:{pessoa1.nome}\nidade:{pessoa1.idade}\npeso{pessoa1.peso}\naltura{pessoa1.altura}")