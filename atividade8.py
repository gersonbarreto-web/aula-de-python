import os
os.system("cls")

print("""
Codigo \t Prato \t valor
    1 \t picanha \t r$ 25,00
    2 \t lasanha \t r$ 25,00
    3 \t strogonof \t r$ 20,00
    4 \t bife acebolado \t r$ 13,00
    5  \t pao com ovo \t r$ 15,00        
""")

codigo= int (input("digite o codigo do prato desejado"))

match codigo:
    case 1:
        print("prata escolhido foi picanha : r$ 25,00 ")
    case 2:
        print("prata escolhido lasanha r$ : 25,00 ")    
    case 3:
        print("prata escolhido foi strogonof  : 20,00 ")    
    case 4:
        print("prata escolhido foi bife acebolado : r$ 13,00 ")

    case 5:
         print("prata escolhido foi pao com ovo : $ 15,00  ")  