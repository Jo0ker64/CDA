# Votre script prend un prix TTC en entrée, indiquez le prix HT du produit. (TVA 20%)

# # Définition du taux de TVA (20%)
# taux_tva = 0.20

# try:
#     # Demande à l'utilisateur d'entrer le prix TTC et le convertit en nombre à virgule flottante
#     prix_ttc = float(input("Entrez le prix TTC du produit : "))
# except ValueError:
#     # Gère l'erreur si l'utilisateur n'entre pas un nombre valide
#     print("Veuillez entrer un nombre valide.")
#     exit()  # Quitte le programme

# # Calcul du prix HT
# prix_ht = prix_ttc / (1 + taux_tva)

# # Calcul du montant de la TVA
# montant_tva = prix_ttc - prix_ht

# # Affichage des résultats avec deux décimales
# print(f"Le prix HT du produit est : {prix_ht:.2f} €")
# print(f"Le montant de la TVA est : {montant_tva:.2f} €")

##################################################################################################################

# Demande à l'utilisateur d'entrer le prix TTC et le convertit en nombre à virgule flottante
prix_ttc = float(input("Entrez le prix TTC : "))

# Calcul du prix HT (en divisant par 1.20 pour un taux de TVA de 20%)
prix_ht = prix_ttc / 1.20

# Calcul du montant de la TVA
montant_tva = prix_ttc - prix_ht

# Affichage du prix HT avec deux décimales
#:.2f dans les f-strings formate les nombres pour afficher deux décimales.
print(f"Le prix HT est : {prix_ht:.2f} €")

# Affichage du montant de la TVA avec deux décimales
#:.2f dans les f-strings formate les nombres pour afficher deux décimales.
print(f"Le montant de la TVA est : {montant_tva:.2f} €")

