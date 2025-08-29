import os
os.system("cls")

macas = float(input("Digite quantas macas voce quer"))

if macas <12:
    valor = macas*1.3
    print(f"o valor da sua compra foi: {valor}")
else:
    print (f"o valor da sua compra foi: {macas}")  

