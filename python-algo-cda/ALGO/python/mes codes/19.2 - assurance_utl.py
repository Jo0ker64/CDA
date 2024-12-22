def obtenir_nombre_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Fonction pour déterminer la catégorie avec prise en compte de la date du dernier accident
def determiner_categorie(annees_permis, nombre_accidents, dernier_accident_annees):
    # Si le dernier accident date de plus de 2 ans et permis supérieur à 10 ans, on ne prend pas en compte cet accident
    if annees_permis >= 10 and dernier_accident_annees > 2:
        nombre_accidents = 0

    # Détermination de la catégorie
    if annees_permis < 2 or nombre_accidents > 3:
        return "Rouge"
    elif 2 <= annees_permis < 5 or (1 <= nombre_accidents <= 2):
        return "Orange"
    elif (5 <= annees_permis < 10 and nombre_accidents <= 1):
        return "Vert"
    else:
        return "Bleu"

# Obtention des informations de l'assuré
annees_permis = obtenir_nombre_entier("Depuis combien d'années avez-vous votre permis ? ")
nombre_accidents = obtenir_nombre_entier("Combien d'accidents avez-vous eu ? ")

# Si accidents, demander le nombre d'années depuis le dernier accident
dernier_accident_annees = 0
if nombre_accidents > 0:
    dernier_accident_annees = obtenir_nombre_entier("Depuis combien d'années avez-vous eu votre dernier accident ? ")

# Détermination de la catégorie
categorie = determiner_categorie(annees_permis, nombre_accidents, dernier_accident_annees)

# Affichage du résultat
print(f"\nRésultat de l'évaluation :")
print(f"Années de permis : {annees_permis}")
print(f"Nombre d'accidents : {nombre_accidents}")
print(f"Années depuis le dernier accident : {dernier_accident_annees}")
print(f"Catégorie d'assurance : {categorie}")

# Explication de la catégorie
if categorie == "Rouge":
    print("Explication : Catégorie à haut risque. Moins de 2 ans de permis ou plus de 3 accidents.")
elif categorie == "Orange":
    print("Explication : Catégorie à risque modéré. Permis entre 2 et 5 ans et/ou entre 1 et 2 accidents.")
elif categorie == "Vert":
    print("Explication : Catégorie à faible risque. Permis entre 5 et 10 ans, avec 0 ou 1 accident.")
elif categorie == "Bleu":
    print("Explication : Catégorie à très faible risque. Plus de 10 ans de permis sans accident récent.")
