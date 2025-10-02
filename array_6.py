import os
os.system("cls")

numeros = []
soma_positivos = 0
quantidade_negativos = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
   
    if numero > 0:
        soma_positivos += numero
    elif numero < 0:
        quantidade_negativos += 1

print("\n= RESULTADO =")

for numero in numeros:
    print(f"Número: {numero}")

print(f"\nSoma de números positivos: {soma_positivos}")
print(f"Quantidade de números negativos: {quantidade_negativos}")  