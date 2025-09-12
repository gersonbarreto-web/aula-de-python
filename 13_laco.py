import os
os.system("cls")


print("laco de repeticao -while")

quantidade_notas = 2
soma = 0 

for i in range (quantidade_notas):
    while True :
        nota = int(input(f"digite a {i+1}ª nota: "))
        if nota >= 0 and nota <= 10:
            break
    soma= soma + nota

media = soma / quantidade_notas

print(f"media:{media}")