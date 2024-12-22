# Calcul de la prime d’assurance basée sur des critères
# Règles :
# Prime de base : Voiture : 500€, Moto : 300€, Camion : 1000€.
# Majoration pour âge du véhicule : +10% si le véhicule a plus de 5 ans.
# Majoration pour kilométrage annuel : +5% si plus de 20 000 km, + 15% si plus de 30 000km


# Fonction pour obtenir une entrée valide pour le type de véhicule
def obtenir_type_vehicule():
    while True:
        type_vehicule = input("Entrez le type de véhicule (Voiture/Moto/Camion) : ").capitalize()
        if type_vehicule in ["Voiture", "Moto", "Camion"]:
            return type_vehicule
        print("Type de véhicule invalide. Veuillez réessayer.")

# Fonction pour obtenir une entrée numérique valide
def obtenir_nombre(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Obtention des informations du véhicule
type_vehicule = obtenir_type_vehicule()
age_vehicule = obtenir_nombre("Entrez l'âge du véhicule en années : ")
kilometrage_annuel = obtenir_nombre("Entrez le kilométrage annuel : ")

# Calcul de la prime de base
if type_vehicule == "Voiture":
    prime = 500
elif type_vehicule == "Moto":
    prime = 300
else:  # Camion
    prime = 1000

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
print(f"Kilométrage annuel : {kilometrage_annuel} km")
print(f"Prime finale : {prime:.2f}€")
