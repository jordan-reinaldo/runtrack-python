montant_initial = 10000  
taux_de_rendement_annuel = 0.10


gain_annuel = montant_initial * taux_de_rendement_annuel

print(f"Gain annuel initial : {gain_annuel:.0f}€")

montant_initial += gain_annuel

print(f" montant total: {montant_initial}")

augmentation_de_capital = 5000
taux_augmentation = 0.02

montant_initial += augmentation_de_capital

print(f"montant total après ajout de fond {montant_initial}€")

taux_de_rendement_annuel += taux_augmentation
gain_annuel = montant_initial * taux_de_rendement_annuel
montant_initial += gain_annuel
print(f"gain annuel {gain_annuel}€")
print(f" montant total: {montant_initial}€")

retrait_capital= 0.9

montant_initial *= retrait_capital

print(f"montant total après retrait : {montant_initial}€")

taux_baisse= 0.01
taux_de_rendement_annuel -= taux_baisse
gain_annuel = montant_initial * taux_de_rendement_annuel
montant_initial += gain_annuel

print(f"gain annuel {gain_annuel}€")
print(f"montant final : {montant_initial}€")