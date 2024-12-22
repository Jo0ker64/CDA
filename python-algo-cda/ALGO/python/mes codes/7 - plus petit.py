# Votre script prend une liste en entrée, indiquez le plus petit élément de la liste

# def obtenir_liste():
#     # Fonction pour obtenir une liste de nombres de l'utilisateur
#     entree = input("Entrez une liste de nombres séparés par des espaces : ")
#     # Convertit l'entrée en une liste d'entiers
#     return [int(x) for x in entree.split()]

# # Appelle la fonction pour obtenir la liste
# liste = obtenir_liste()

# # Vérifie si la liste n'est pas vide
# if liste:
#     # Trouve le plus petit élément de la liste
#     plus_petit = min(liste)
#     # Affiche le résultat
#     print(f"Le plus petit élément de la liste est : {plus_petit}")
# else:
#     # Message si la liste est vide
#     print("La liste est vide.")

#################################################################################################
# Demande à l'utilisateur d'entrer une liste de nombres et la convertit immédiatement en liste d'entiers
# input() récupère l'entrée de l'utilisateur
# split() divise la chaîne en une liste de sous-chaînes, en utilisant l'espace comme séparateur
# [int(x) for x in ...] est une compréhension de liste qui convertit chaque élément en entier
liste = [int(x) for x in input("Entrez une liste de nombres séparés par des espaces : ").split()]

# Affiche le plus petit élément de la liste
# min() trouve le plus petit élément de la liste
# f-string est utilisée pour formater la sortie
print(f"Le plus petit élément est : {min(liste)}")

