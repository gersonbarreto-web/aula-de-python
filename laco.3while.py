import os
os.system("cls")

quantidade= 0
soma = 0

while True:
    n=float(input(f"digite um numero: ") )
    if n <0 :
        break
    quantidade+=1
    soma+= n

media = soma / quantidade

print(f"\nMedia:{media}")
