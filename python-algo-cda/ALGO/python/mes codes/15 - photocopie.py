# Votre script prend en entrée un nombre de photocopies a faire, indiquez le prix de la
# commande en sachant que :
# 1. de 1 à 10 photocopies le prix est de 0.20€ par page
# 2. de 11 à 30 photocopies le prix est de 0.15€ par page
# 3. de 31 à n photocopies le prix est de 0.10€ par page

######################################   PRIX A L'UNITÉ   #################################################
# try:
#     # Demande à l'utilisateur d'entrer le nombre de photocopies et le convertit en entier
#     nombre_photocopies = int(input("Entrez le nombre de photocopies à faire : "))
#     # Vérifie si le nombre est positif
#     if nombre_photocopies <= 0:
#         # Lève une exception si le nombre n'est pas positif
#         raise ValueError("Le nombre de photocopies doit être positif.")
# except ValueError as e:
#     # Capture et affiche l'erreur si la saisie n'est pas valide ou si le nombre n'est pas positif
#     print(f"Erreur : {e}")
#     # Quitte le programme en cas d'erreur
#     exit()

# # Initialise la variable pour le prix total
# prix_total = 0

# # Calcule le prix total en fonction du nombre de photocopies
# if nombre_photocopies <= 10:
#     # 0.20€ par copie pour les 10 premières
#     prix_total = nombre_photocopies * 0.20
# elif nombre_photocopies <= 30:
#     # 0.20€ pour les 10 premières, puis 0.15€ pour les suivantes jusqu'à 30
#     prix_total = 10 * 0.20 + (nombre_photocopies - 10) * 0.15
# else:
#     # 0.20€ pour les 10 premières, 0.15€ pour les 20 suivantes, puis 0.10€ pour le reste
#     prix_total = 10 * 0.20 + 20 * 0.15 + (nombre_photocopies - 30) * 0.10

# # Affiche le prix total
# print(f"Pour {nombre_photocopies} photocopies, le prix total est de : {prix_total:.2f} €")

# # Affiche le détail du calcul pour plus de 30 copies
# if nombre_photocopies > 30:
#     print("Détail du calcul :")
#     print(f"  10 premières copies à 0.20€ : {10 * 0.20:.2f} €")
#     print(f"  20 copies suivantes à 0.15€ : {20 * 0.15:.2f} €")
#     print(f"  {nombre_photocopies - 30} dernières copies à 0.10€ : {(nombre_photocopies - 30) * 0.10:.2f} €")
# # Affiche le détail du calcul pour 11 à 30 copies
# elif nombre_photocopies > 10:
#     print("Détail du calcul :")
#     print(f"  10 premières copies à 0.20€ : {10 * 0.20:.2f} €")
#     print(f"  {nombre_photocopies - 10} copies suivantes à 0.15€ : {(nombre_photocopies - 10) * 0.15:.2f} €")
#     print(f"Le prix pour {nombre_photocopies} photocopies est de {prix_total:.2f}€")


#########################################    PRIX A L'UNITÉ   #########################################

"""Demande à l'utilisateur d'entrer le nombre de photocopies et le convertit en entier"""
# nombre_photocopies = int(input("Entrez le nombre de photocopies : "))

"""Calcule le prix total en fonction du nombre de photocopies"""
# if nombre_photocopies <= 10:
"""  Si 10 photocopies ou moins, le prix est de 0.20€ par copie"""
        #prix = nombre_photocopies * 0.20
# elif nombre_photocopies <= 30:
"""Si entre 11 et 30 photocopies :
0.20€ pour les 10 premières, puis 0.15€ pour les suivantes"""
        # prix = 10 * 0.20 + (nombre_photocopies - 10) * 0.15
# else:
"""Si plus de 30 photocopies :
0.20€ pour les 10 premières,
0.15€ pour les 20 suivantes,
0.10€ pour le reste"""
       # prix = 10 * 0.20 + 20 * 0.15 + (nombre_photocopies - 30) * 0.10

"""Affiche le prix total formaté avec deux décimales"""
# print(f"Le prix total est : {prix:.2f} €")



######################################## EN RPIX DE GROS ##############################""

# Demande à l'utilisateur d'entrer le nombre de photocopies et le convertit en entier
nombre_photocopie = int(input("Entrez le nombre de photocopies : "))

# Calcule le prix total en fonction du nombre de photocopies
if nombre_photocopie <= 10:
    # Si 10 photocopies ou moins, le prix est de 0.20€ par copie
    prix = nombre_photocopie * 0.20
elif 11 <= nombre_photocopie <= 30:
    # Si entre 11 et 30 photocopies incluses, le prix est de 0.15€ par copie
    prix = nombre_photocopie * 0.15
else:
    # Si plus de 30 photocopies, le prix est de 0.10€ par copie
    prix = nombre_photocopie * 0.10

# Affiche le prix total formaté avec deux décimales
print(f"Le prix total est : {prix:.2f} €")
