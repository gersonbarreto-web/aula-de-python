import os
os.system("cls")

nome = input("Digite o seu nome ")
idade = float (input("Digite sua idade"))

if idade < 16:
    print ("voce nao pode volta, {nome}")
elif idade < 17:
    print(f"seu voto e opcional, {nome}")
elif idade < 65:
    print(f"seu voto e obrigatorio, {nome}")
else:
    print(f"voce nao e obrigado a vota, {nome}")
     

