import os
os.system("cls")

nome = input ("Digite seu nome ")
n1=float (input("Digite a primeira nota"))
n2= float (input("Digite a segunda nota"))
media=("n1+n2")/2

if media >4:
    conceito = "E"
elif media < 6:
    conceito= "D"
elif media <7.5:
    conceito= "c"
elif media <9:
    conceito="B"
elif media <=10:
    conceito = "A"

if media >6:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"media:{media}")
print(F"conceito:{conceito}")
print(f"resultado:{resultado}")
      