def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur: Division par zéro"
    elif operator == '%':
        return num1 % num2
    else:
        return "Opérateur invalide"
resultat = calcule(12, "%", 3)
print(resultat)