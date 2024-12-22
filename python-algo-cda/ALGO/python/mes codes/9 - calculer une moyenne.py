# Votre script prend une liste de notes en entrée, indiquez la moyenne de la liste.

# def obtenir_notes():
#     # Demande à l'utilisateur d'entrer les notes
#     entree = input("Entrez une liste de notes séparées par des espaces (utilisez la virgule pour les décimales) : ")

#     # Remplace les virgules par des points pour la conversion en float
#     entree = entree.replace(',', '.')
#     # Convertit l'entrée en une liste de nombres flottants
#     return [float(x) for x in entree.split()]

# # Appelle la fonction pour obtenir les notes
# notes = obtenir_notes()

# # Vérifie si la liste de notes n'est pas vide
# if notes:
#     # Calcule la moyenne des notes
#     moyenne = sum(notes) / len(notes)
#     # Formate la moyenne avec 2 décimales et remplace le point par une virgule
#     moyenne_str = f"{moyenne:.2f}".replace('.', ',')
#     # Affiche la moyenne
#     print(f"La moyenne des notes est : {moyenne_str}")
# else:
#     # Message si la liste est vide
#     print("La liste de notes est vide.")

# # Affiche les notes saisies si la liste n'est pas vide
# if notes:
#     print("Notes saisies :")
#     for note in notes:
#         # Formate chaque note avec 2 décimales et remplace le point par une virgule
#         note_str = f"{note:.2f}".replace('.', ',')
#         print(note_str)


#############################################################################################################
# Demande à l'utilisateur d'entrer les notes et les convertit immédiatement en liste de nombres flottants
# input() récupère l'entrée de l'utilisateur
# split() divise la chaîne en une liste de sous-chaînes, en utilisant l'espace comme séparateur
# [float(x) for x in ...] est une compréhension de liste qui convertit chaque élément en nombre flottant
"""notes = [float(x) for x in input("Entrez les notes séparées par des espaces : ").split()]"""

# Calcule la moyenne des notes
# sum(notes) additionne toutes les notes
# len(notes) donne le nombre de notes
# La division donne la moyenne
"""moyenne = sum(notes) / len(notes)"""

# Affiche la moyenne
# f-string est utilisée pour formater la sortie
"""print(f"La moyenne est : {moyenne}")"""

#############################################################################################################

# Demande à l'utilisateur d'entrer les notes
entree = input("Entrez une liste de notes séparées par des espaces (utilisez la virgule pour les décimales) : ")

# Remplace les virgules par des points pour la conversion en float
entree = entree.replace(',', '.')

# Convertit l'entrée en une liste de nombres flottants
notes = [float(x) for x in entree.split()]

# Vérifie si la liste de notes n'est pas vide
if notes:
    # Initialisation des variables pour la somme et le compteur
    somme = 0.0
    compteur = 0

    # Calcule la somme et le compteur des notes
    for note in notes:
        somme += note
        compteur += 1

    # Calcule la moyenne
    moyenne = somme / compteur
    # Formate la moyenne avec 2 décimales et remplace le point par une virgule
    moyenne_str = f"{moyenne:.2f}".replace('.', ',')
    # Affiche la moyenne
    print(f"La moyenne des notes est : {moyenne_str}")

    # Affiche les notes saisies
    print("Notes saisies :")
    for note in notes:
        # Formate chaque note avec 2 décimales et remplace le point par une virgule
        note_str = f"{note:.2f}".replace('.', ',')
        print(note_str)
else:
    # Message si la liste est vide
    print("La liste de notes est vide.")