# #Élimination des doublons dans une liste :
# Ecrire un script qui supprime tous les doublons dans une liste, attention l’ordre doit rester le même

# Définition d'une liste d'exemple contenant des doublons
liste = [1, 2, 3, 1, 2, 4, 5, 3, 6]  # Exemple de liste avec des doublons

# Création d'une nouvelle liste vide pour stocker les éléments uniques
nouvelle_liste = []

# Boucle parcourant chaque élément de la liste originale
for element in liste:
    # Vérifie si l'élément n'est pas déjà dans la nouvelle liste
    if element not in nouvelle_liste:
        # Si l'élément est nouveau, l'ajoute à la nouvelle liste
        nouvelle_liste.append(element)

# Affiche la nouvelle liste sans doublons
print("Liste sans doublons :", nouvelle_liste)

