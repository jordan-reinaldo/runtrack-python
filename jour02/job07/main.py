chaine = "abcdefghijklmnopqrstuvwxyz" * 10

lettre = 1

while lettre <= len(chaine):

    print(chaine[:lettre])

    lettre += 2

    if lettre > len(chaine):
        break




#autre manière de faire sans while

# chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# for i in range(1, len(chaine), 2):
    # print(chaine[:i])