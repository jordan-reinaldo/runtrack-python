chaine = "abcdefghijklmnopqrstuvwxyz" * 10

lettre = 1

while lettre <= len(chaine):

    print(chaine[:lettre])

    lettre += 2

    if lettre > len(chaine):
        break