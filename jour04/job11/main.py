def list_up1(liste):
    return [i + 1 for i in liste]

L=[7, 11, 42, 39, 2]

L_up1 = list_up1(L)

print(L_up1)

# ci-dessous test de la fonction pour vérifier compréhension, on prend la nouvelle liste (celle demandé par l'exercice comme paramètre)

L_up2 = list_up1(L_up1)


print(L_up2)



# autre manière de faire l'exercice :
# L = [7, 11, 42, 39, 2]
# longueur_liste = len(L)

# for i in range (0, longueur_liste) :
    #  L[i] = L[i] + 1
# print (F"L modifiee par ajout de 1 : {L} ")