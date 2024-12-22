types_valides = {"Voiture": 500, "Moto": 300, "Camion": 1000}

# Obtention du type de véhicule
while True:
    type_vehicule = input("Entrez le type de véhicule (Voiture/Moto/Camion) : ").capitalize()
    if type_vehicule in types_valides:
        prime = types_valides[type_vehicule]
        break
    print("Type de véhicule invalide. Veuillez réessayer.")

# Obtention de l'âge du véhicule
while True:
    try:
        age_vehicule = float(input("Entrez l'âge du véhicule en années : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Obtention du kilométrage annuel
while True:
    try:
        kilometrage_annuel = float(input("Entrez le kilométrage annuel : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Majoration pour l'âge du véhicule
if age_vehicule > 5:
    prime *= 1.10  # +10%

# Majoration pour le kilométrage annuel
if kilometrage_annuel > 30000:
    prime *= 1.15  # +15%
elif kilometrage_annuel > 20000:
    prime *= 1.05  # +5%

# Affichage du résultat
print(f"\nPrime d'assurance pour votre {type_vehicule} :")
print(f"Prime de base : {prime:.2f}€")
print(f"Âge du véhicule : {age_vehicule} ans")
print(f"Kilométrage annuel : {kilometrage_annuel:.2f} km")
print(f"Prime finale : {prime:.2f}€")