# Obtention des informations de l'assuré
while True:
    try:
        annees_permis = int(input("Depuis combien d'années avez-vous votre permis ? "))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

while True:
    try:
        nombre_accidents = int(input("Combien d'accidents avez-vous eu ? "))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Détermination de la catégorie
if annees_permis < 2 or nombre_accidents > 3:
    categorie = "Rouge"
elif 2 <= annees_permis < 5 or (1 <= nombre_accidents <= 2):
    categorie = "Orange"
elif 5 <= annees_permis < 10 and nombre_accidents <= 1:
    categorie = "Vert"
elif annees_permis >= 10 and nombre_accidents == 0:
    categorie = "Bleu"
else:
    categorie = "Rouge"  # Cette clause inclut tous les autres cas

# Affichage du résultat
print(f"\nRésultat de l'évaluation :")
print(f"Années de permis : {annees_permis}")
print(f"Nombre d'accidents : {nombre_accidents}")
print(f"Catégorie d'assurance : {categorie}")

# Explication de la catégorie
if categorie == "Rouge":
    print("Explication : Catégorie à haut risque. Moins de 2 ans de permis ou plus de 3 accidents.")
elif categorie == "Orange":
    print("Explication : Catégorie à risque modéré. Permis entre 2 et 5 ans et/ou entre 1 et 2 accidents.")
elif categorie == "Vert":
    print("Explication : Catégorie à faible risque. Permis entre 5 et 10 ans, avec 0 ou 1 accident.")
elif categorie == "Bleu":
    print("Explication : Catégorie à très faible risque. Plus de 10 ans de permis sans accident.")