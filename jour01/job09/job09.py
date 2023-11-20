nom_produit = "TV"
quantite_en_stock = 30
prix_unitaire = 500

print("Informations du produit:")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire}€")
print(f"Quantité en stock : {quantite_en_stock} unités")

quantite_achetee = int(input("Combien d'unités de TV souhaitez-vous acheter ? "))

quantite_en_stock -= quantite_achetee
print(f"Vous avez acheté {quantite_achetee} unité(s) de {nom_produit}.")

prix_unitaire *= 1.1

print("\nInformations mises à jour du produit:")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire actualisé: {prix_unitaire}€")
print(f"Quantité en stock : {quantite_en_stock} unités")