def distance_parcourue_par_semaine(nombre_marches, hauteur_marche_cm):

    nombre_allers_retours_par_jour = 5 * 2

    hauteur_marche_m = hauteur_marche_cm / 100

    distance_par_montee_descente = nombre_marches * hauteur_marche_m

    distance_par_jour = distance_par_montee_descente * nombre_allers_retours_par_jour

    distance_par_semaine = distance_par_jour * 7 

    return distance_par_semaine

# test fonction
nombre_marches = 100 
hauteur_marche_cm = 20 
distance_semaine = distance_parcourue_par_semaine(nombre_marches, hauteur_marche_cm)
print(f"Pour {nombre_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_semaine:.2f} m par semaine.")