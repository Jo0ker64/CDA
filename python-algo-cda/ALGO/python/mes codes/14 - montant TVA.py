# Votre script prend en entrée un prix HT, indiquez le montant de la TVA (5%)

# # Définition du taux de TVA (5%)
# taux_tva = 0.05  # 5%

# try:
#     # Demande à l'utilisateur d'entrer le prix HT et le convertit en nombre à virgule flottante
#     prix_ht = float(input("Entrez le prix HT du produit : "))
# except ValueError:
#     # Gère l'erreur si l'utilisateur n'entre pas un nombre valide
#     print("Veuillez entrer un nombre valide.")
#     exit()  # Quitte le programme

# # Calcul du montant de la TVA
# montant_tva = prix_ht * taux_tva

# # Calcul du prix TTC
# prix_ttc = prix_ht + montant_tva

# # Affichage des résultats avec deux décimales
# print(f"Prix HT : {prix_ht:.2f} €")
# print(f"Montant de la TVA (5%) : {montant_tva:.2f} €")
# print(f"Prix TTC : {prix_ttc:.2f} €")

################################################################################################################

# Demande à l'utilisateur d'entrer le prix HT et le convertit en nombre à virgule flottante
prix_ht = float(input("Entrez le prix HT : "))

# Calcul du montant de la TVA (20% du prix HT)
tva = prix_ht * 0.20

# Calcul du prix TTC (prix HT + montant de la TVA)
prix_ttc = prix_ht + tva

# Affichage du montant de la TVA avec deux décimales
print(f"Le montant de la TVA est : {tva:.2f} €")

# Affichage du prix TTC avec deux décimales
print(f"Le prix TTC est de : {prix_ttc:.2f}€")

