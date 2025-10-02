import os 
os.system("cls")

lista_numeros = []

print("solicitando 5 numeros. ")
for i in range(5):
    numero = float(input("DIGITE UM NUMERO:"))
    lista_numeros.append(numero)

menor = min(lista_numeros)
maior = max(lista_numeros)

print("mostrando todos os numeros")
for i in range (5):
    print(f"numero:{lista_numeros[i]}")

print(f"n\menor numero:{menor}")
print(f"maior numero: {maior}")