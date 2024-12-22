# Votre script prend une liste en entrée, indiquez la somme des nombres pairs dans la liste


# Définition d'une fonction pour obtenir une liste de nombres de l'utilisateur
# def obtenir_liste():
#     # Demande à l'utilisateur d'entrer des nombres séparés par des espaces
#     entree = input("Entrez une liste de nombres entiers séparés par des espaces : ")
#     # Convertit l'entrée en une liste d'entiers
#     return [int(x) for x in entree.split()]

# # Appel de la fonction pour obtenir la liste
# liste = obtenir_liste()

# # Calcul de la somme des nombres pairs dans la liste
# somme_pairs = sum(nombre for nombre in liste if nombre % 2 == 0)

# # Vérification si la liste n'est pas vide
# if liste:
#     # Affichage de la somme des nombres pairs
#     print(f"La somme des nombres pairs dans la liste est : {somme_pairs}")
    
#     # Création d'une liste des nombres pairs (convertis en chaînes)
#     nombres_pairs = [str(nombre) for nombre in liste if nombre % 2 == 0]
#     # Vérification s'il y a des nombres pairs
#     if nombres_pairs:
#         # Affichage des nombres pairs
#         print(f"Les nombres pairs dans la liste sont : {', '.join(nombres_pairs)}")
#     else:
#         # Message si aucun nombre pair n'est trouvé
#         print("Aucun nombre pair n'a été trouvé dans la liste.")
# else:
#     # Message si la liste est vide
#     print("La liste est vide.")

###############################################################################################################

# Demande à l'utilisateur d'entrer une liste de nombres et la convertit en liste d'entiers
liste = [int(x) for x in input("Entrez une liste de nombres séparés par des espaces : ").split()]

# Calcule la somme des nombres pairs dans la liste
somme = sum(num for num in liste if num % 2 == 0)

# Affiche le résultat
print(f"La somme des nombres pairs est : {somme}")

