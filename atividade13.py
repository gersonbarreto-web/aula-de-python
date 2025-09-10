import os
os.system("cls")

altura = float (input("digite sua altuta"))
sexo= input("digite o seu sexo (digite M pra masculino e F pra femenino)")

match sexo:
    
    case "M":
        print(f" o peso idela para voce e de {72.7 *altura-58} ")
    case "F":
        print(f"o peso idela para voce e de {62.1 * altura - 44.7}")