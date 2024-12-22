# Vérification saisie utilisateur (utilisation d’une boucle while)
# Ecrire un script qui vérifie que l’utilisateur saisie un nombre qui est compris
# dans l’intervalle 1 a 100
# Tant que l’utilisateurs n’as pas saisie un nombre dans l’intervalle le script doit
# reproposer un prompt 

def est_nombre_valide(saisie):
    """Vérifie si la saisie est un nombre entier entre 1 et 100."""
    try:
        nombre = int(saisie)
        return 1 <= nombre <= 100
    except ValueError:
        return False

# Initialisation de la variable pour stocker la saisie de l'utilisateur
saisie_utilisateur = ""

# Boucle while pour continuer à demander jusqu'à ce qu'une saisie valide soit entrée
while not est_nombre_valide(saisie_utilisateur):
    saisie_utilisateur = input("Veuillez entrer un nombre entre 1 et 100 : ")
    
    if not est_nombre_valide(saisie_utilisateur):
        print("Erreur : Veuillez entrer un nombre entier valide entre 1 et 100.")

# Conversion de la saisie en nombre entier
nombre_final = int(saisie_utilisateur)

# Affichage du résultat
print(f"Vous avez saisi le nombre valide : {nombre_final}")
