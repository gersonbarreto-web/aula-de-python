import os
os.system("cls")

numero1 = float (input("Digite um numero"))
numero2 = float(input("Digite o segundo numero"))

soma = numero1 + numero2
produto = numero1 * numero2

if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1
   print(f"soma: {soma}")
   print(f"produto: {produto}")    
   print(f"maior numero: {maior}")
   print(f"menor numero : {menor}")