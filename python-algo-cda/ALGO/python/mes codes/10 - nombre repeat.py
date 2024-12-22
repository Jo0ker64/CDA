# Votre script prend une liste de nombres en entrée, indiquez le nombre qui se répète le plus de fois dans la liste

# Définition de la liste de nombres
# numbers = [11, 12, 11, 9, 1, 5, 4, 6, 12, 12, 10, 6, 6, 11, 12, 11, 9, 1, 5, 4, 6, 12, 12, 10, 6, 6]

# Initialisation d'un dictionnaire vide pour compter les occurrences de chaque nombre
# count_dict = {}

# Boucle pour compter les occurrences de chaque nombre dans la liste
# for number in numbers:
#     if number in count_dict:
#         # Si le nombre est déjà dans le dictionnaire, on incrémente son compteur
#         count_dict[number] += 1
#     else:
#         # Si le nombre n'est pas dans le dictionnaire, on l'ajoute avec un compteur de 1
#         count_dict[number] = 1

# Initialisation des variables pour trouver le nombre le plus fréquent
# most_common_number = None  # Stockera le nombre le plus fréquent
# max_count = -1  # Stockera le nombre maximal d'occurrences

# Boucle pour trouver le nombre avec le plus grand nombre d'occurrences
# for number, count in count_dict.items():
#     if count > max_count:
#         # Si le compte actuel est supérieur au maximum précédent,
#         # on met à jour le maximum et le nombre le plus fréquent
#         max_count = count
#         most_common_number = number

# Affichage du résultat
# print(f"Le nombre qui se répète le plus est {most_common_number} avec {max_count} occurrences.")

###########################################################################################################
# Importation de la classe Counter du module collections
# from collections import Counter

# Définition d'une fonction pour obtenir une liste de nombres de l'utilisateur
# def obtenir_liste():
#     # Demande à l'utilisateur d'entrer des nombres séparés par des espaces
#     entree = input("Entrez une liste de nombres séparés par des espaces : ")
#     # Convertit l'entrée en une liste d'entiers
#     return [int(x) for x in entree.split()]

# Appel de la fonction pour obtenir la liste de l'utilisateur
# liste = obtenir_liste()

# Vérifie si la liste n'est pas vide
# if liste:
#     # Crée un objet Counter à partir de la liste
#     compteur = Counter(liste)
    
#     # Obtient le nombre le plus fréquent et son nombre d'occurrences
#     nombre_plus_frequent, occurrences = compteur.most_common(1)[0]
    
#     # Affiche le nombre le plus fréquent et son nombre d'occurrences
#     print(f"Le nombre qui se répète le plus est : {nombre_plus_frequent}")
#     print(f"Il apparaît {occurrences} fois dans la liste.")
    
#     # Trouve tous les nombres qui apparaissent le même nombre de fois que le plus fréquent
#     tous_plus_frequents = [num for num, count in compteur.items() if count == occurrences]
#     # S'il y a plus d'un nombre avec le même nombre maximal d'occurrences
#     if len(tous_plus_frequents) > 1:
#         print("Note : Il y a une égalité. Les nombres suivants apparaissent le même nombre de fois :")
#         # Affiche tous ces nombres, séparés par des virgules
#         print(", ".join(map(str, tous_plus_frequents)))
# else:
#     # Si la liste est vide, affiche un message
#     print("La liste est vide.")


##########################################################################################################
# Importation de la classe Counter du module collections
# from collections import Counter

# Demande à l'utilisateur d'entrer une liste de nombres et la convertit en liste d'entiers
# input() récupère l'entrée de l'utilisateur sous forme de chaîne
# split() divise cette chaîne en une liste de sous-chaînes, en utilisant l'espace comme séparateur
# [int(x) for x in ...] est une compréhension de liste qui convertit chaque sous-chaîne en entier
# liste = [int(x) for x in input("Entrez une liste de nombres séparés par des espaces : ").split()]

# Crée un objet Counter à partir de la liste
# Counter compte automatiquement les occurrences de chaque élément dans la liste
# compteur = Counter(liste)

# Affiche le nombre le plus répété
# most_common(1) retourne une liste contenant un tuple (élément, nombre d'occurrences) pour l'élément le plus fréquent
# [0][0] accède au premier élément de cette liste (le tuple), puis au premier élément de ce tuple (le nombre lui-même)
# print(f"Le nombre le plus répété est : {compteur.most_common(1)[0][0]}")

###########################################################################################

# Définition de la liste initiale de nombres
listes = [45, 12, 60, 8, 61, 60, 60, 8, 12, 8, 60, 12, 60, 12, 8, 8, 8, 8, 12,60, 60 , 60, 60]

# Initialisation d'une nouvelle liste pour stocker les éléments uniques
nls = []

# Boucle pour créer une liste d'éléments uniques
for element in listes:
    # Si l'élément ne se trouve pas dans la nouvelle liste, on l'ajoute
    if element not in nls:
        nls.append(element)

# Initialisation des variables pour le comptage
x = 0  # Compteur temporaire
z = 0  # Compteur maximum

# Boucle principale pour trouver l'élément le plus fréquent
for nb in listes:
    # Si nb se trouve dans la liste des éléments uniques
    if nb in nls:
        # On incrémente le compteur temporaire
        x += 1
        # Si le compteur temporaire est plus grand que le compteur maximum
        if x > z:
            # On stocke la valeur actuelle comme résultat potentiel
            result = nb
            # On met à jour le compteur maximum
            z = x
        # On réinitialise le compteur temporaire pour le prochain élément
        x = 0

# Affichage du résultat (l'élément supposé être le plus fréquent)
print(result)


