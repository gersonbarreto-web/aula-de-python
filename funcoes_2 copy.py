import os


def logo_senai():
    os.system("cls")
    print("=======")
    print("= SENAI =")
    print("=========")

logo_senai()
nome = input("digite seu nome: ")
logo_senai()
idade = int(input("digite sua idade "))
logo_senai()
peso = float(input("digite seu peso"))

logo_senai()
print(f"nome : {nome}")
print(f"idade: {idade}")
print(f"peso:  {peso} ")



