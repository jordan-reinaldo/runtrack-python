L = [10, 8, 9, 12, 15, 17, 13]

# Fonction pour calculer la longueur de la liste sans utiliser la fonction système len()
def longueur(liste):
    compteur = 0
    for i in liste:
        compteur += 1
    return compteur

# Fonction pour trier la liste dans l'ordre croissant sans utiliser de fonctions système
def trier_fsysteme(liste):
    while echange:
        echange = False
        for element in range(1, longueur(liste)):
            if liste[element-1] > liste[element]:
                liste[element-1], liste[element] = liste[element], liste[element-1]
                echange = True
    return liste

print(trier_fsysteme(L))