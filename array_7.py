import os
os.system("cls")

numeros = []
positivos = 0
negativos = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    if numero < 0:
        numero = 0
    numeros.append(numero)    

for numero in numeros:
    print(f"numero {numero}")