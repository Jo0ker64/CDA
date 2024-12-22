# Définition de la fonction pour calculer une remise
def calcul_remise(_montant, _remise): 
    # Calcul du prix après remise
    resultat = _montant - _montant * (_remise/100)
    # Affichage du résultat
    return print("Le prix de l'article après la remise est de : " + str(resultat) + " €")

if __name__ == "__main__":
    calcul_remise()