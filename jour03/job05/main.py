def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Gérer la division par zéro pour éviter une exception
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == "%":
        # Gérer la division par zéro pour éviter une exception
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Division par zéro"
    else:
        return "Opérateur non valide"

# Exemples d'appels de la fonction
result1 = calcule(5, "+", 3)
result2 = calcule(10, "*", 2)
result3 = calcule(8, "/", 4)

# Affichage des résultats
print(result1)
print(result2)
print(result3)