L=[7, 11, 42, 39, 2]

def list_add1(liste):
    return [i + 1 for i in liste]

L_add1 = list_add1(L)

print(L_add1)

# ci-dessous test de la fonction pour vérifier compréhension, on prend la nouvelle liste (celle demandé par l'exercice comme paramètre)

L_add2 = list_add1(L_add1)


print(L_add2)



# autre manière de faire l'exercice :
# L = [7, 11, 42, 39, 2]
# longueur_liste = len(L)

# for i in range (0, longueur_liste) :
    #  L[i] = L[i] + 1
# print (F"L modifiee par ajout de 1 : {L} ")