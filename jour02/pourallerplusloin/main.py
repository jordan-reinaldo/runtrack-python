a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))


if a+b>c and a+c>b and b+c>a: 
    if  a==b==c:
        resultat="équilatéral"

    elif a==b or a==c or b==c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            resultat="triangle isocèle rectangle"

        else: resultat="triangle isocèle"

    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        resultat="triangle rectangle"
    else: resultat="triangle quelconque"
else: resultat="après évaluation, a, b et c ne peuvent pas former un triangle"

print(f"Avec les longueurs a={a}, b={b}, c={c}, le triangle est : {resultat}.")



# Exemple de résolution de l'exercice avec la fonction def.
# a = float(input("Entrez la longueur a : "))
# b = float(input("Entrez la longueur b : "))
# c = float(input("Entrez la longueur c : "))

# def triangle(x, y, z):
    # return x + y > z and x + z > y and y + z > x

# def type_triangle(x, y, z):
    # if triangle(x, y, z):
        # if x == y == z:
            # return "équilatéral"
        # elif x == y or y == z or z == x:
            # if x**2 + y**2 == z**2 or y**2 + z**2 == x**2 or z**2 + x**2 == y**2:
                # return "rectangle isocèle"
            # else:
                # return "isocèle"
        # elif x**2 + y**2 == z**2 or y**2 + z**2 == x**2 or z**2 + x**2 == y**2:
            # return "rectangle"
        # else:
            # return "quelconque"
    # else:
        # return "après évaluation, a, b et c ne peuvent pas former un triangle."

# resultat = type_triangle(a, b, c)

# print(f"Avec les longueurs a={a}, b={b}, c={c}, le triangle est : {resultat}.")