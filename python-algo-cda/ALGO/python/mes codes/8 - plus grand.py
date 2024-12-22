# Votre script prend une liste en entrée, indiquez le plus grand élément de la liste


# def obtenir_liste():
#     # Fonction pour obtenir une liste de nombres de l'utilisateur
#     entree = input("Entrez une liste de nombres séparés par des espaces : ")
#     # Convertit l'entrée en une liste d'entiers
#     return [int(x) for x in entree.split()]

# # Appelle la fonction pour obtenir la liste
# liste = obtenir_liste()

# # Vérifie si la liste n'est pas vide
# if liste:
#     # Trouve le plus grand élément de la liste
#     plus_grand = max(liste)
#     # Affiche le résultat
#     print(f"Le plus grand élément de la liste est : {plus_grand}")
# else:
#     # Message si la liste est vide
#     print("La liste est vide.")


#############################################################################################################
# Demande à l'utilisateur d'entrer une liste de nombres et la convertit immédiatement en liste d'entiers
# input() récupère l'entrée de l'utilisateur
# split() divise la chaîne en une liste de sous-chaînes, en utilisant l'espace comme séparateur
# [int(x) for x in ...] est une compréhension de liste qui convertit chaque élément en entier
liste = [int(x) for x in input("Entrez une liste de nombres séparés par des espaces : ").split()]

# Affiche le plus grand élément de la liste
# max() trouve le plus grand élément de la liste
# f-string est utilisée pour formater la sortie
# sans utiliser f_string il aurait fallu écrire la sortie :
            # print("Le plus grand élément est : " + str(max(liste)))
    #ou
            #print("Le plus grand élément est : {}".format(max(liste)))
#L'utilisation de f-strings rend le code plus facile à lire et à écrire, surtout quand on insère plusieurs valeurs dans une chaîne.
print(f"Le plus grand élément est : {max(liste)}")

