# Votre script demande un mot a l’utilisateur en entrée, indiquez le nombre de voyelle que le mot contient

# Définit une chaîne contenant toutes les voyelles, y compris les voyelles accentuées,
# en minuscules et en majuscules
voyelles = 'aeiouyâàéèêùîôûAEIOUYÂÀÉÈÊÎÔÛ'

# Demande à l'utilisateur d'entrer un mot et le stocke dans la variable 'mot'
mot = input("Entrez un mot : ")

# Initialise un compteur pour le nombre de voyelles trouvées
nombre_voyelles = 0
# Initialise une liste vide pour stocker les voyelles trouvées
voyelles_trouvees = []

# Parcourt chaque lettre du mot entré
for lettre in mot:
    # Vérifie si la lettre est présente dans la chaîne 'voyelles'
    if lettre in voyelles:
        # Si c'est une voyelle, incrémente le compteur
        nombre_voyelles += 1
        # Ajoute la voyelle trouvée à la liste
        voyelles_trouvees.append(lettre)

# Affiche le nombre total de voyelles trouvées dans le mot
# Utilise une f-string pour formater la chaîne de sortie
print(f"Le mot '{mot}' contient {nombre_voyelles} voyelle(s).")

# Affiche les voyelles trouvées
# join() est utilisé pour créer une chaîne à partir de la liste, séparée par des virgules et des espaces
print("Voyelles trouvées :", ', '.join(voyelles_trouvees))
