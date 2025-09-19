# Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota,
# se a resposta do usuário for “N”, o programa fará a média aritmética das notas informadas
# e mostrará a média aritmética para o usuário.
# Obs.: Use um contador dentro do laço de repetição para contar a quantidade de iterações (loops).

import os
os.system("cls")

soma = 0
quantidade_notas = 0

while True:
    nota = float(input("Digite uma nota: "))
    quantidade_notas += 1
    soma += nota
    resposta = input("Deseja inserir mais uma nota? \nUse S ou N: ").lower()
    if resposta == "n":
        break

media = soma / quantidade_notas

print(f"\nMédia: {media}")