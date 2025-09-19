import os
os.system("cls")

dia = input("Digite um numero para o dia da semana: ")

  match dia:
    case 1:
      print("Domingo")
    case 2:
      print("segunda feira")
    case 3:
      print("terca feira")
    case 4:
      print("quarta feira")
    case 5:
      print("quinta feira")
    case 6:
      print("sexta feira")
    case 7:
      print("sabado")
    case _:
      print("Opcao invalida")
  
    print("fim")
  