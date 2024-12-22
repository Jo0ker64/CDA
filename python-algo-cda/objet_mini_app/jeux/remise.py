class RemiseCalculator:
    def __init__(self, montant, remise):
        """
        Initialise le calculateur de remise avec un montant et un pourcentage de remise.
        
        :param montant: Le montant initial de l'article.
        :param remise: Le pourcentage de remise à appliquer.
        """
        self.montant = montant
        self.remise = remise

    def calculer(self):
        """
        Calcule le prix après application de la remise et retourne le résultat.
        
        :return: Le prix de l'article après application de la remise.
        """
        # Calcul du prix après remise
        resultat = self.montant - self.montant * (self.remise / 100)
        
        # Retourne le résultat formaté
        return resultat

    def afficher_resultat(self):
        """
        Affiche le prix de l'article après application de la remise.
        """
        # Appelle la méthode de calcul et affiche le résultat
        resultat = self.calculer()
        print(f"Le prix de l'article après la remise est de : {resultat} €")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de RemiseCalculator avec des valeurs d'exemple
    montant = float(input("Entrez le montant : "))
    remise = float(input("Entrez la remise en % : "))
    calculateur = RemiseCalculator(montant, remise)
    
    # Affiche le résultat
    calculateur.afficher_resultat()
