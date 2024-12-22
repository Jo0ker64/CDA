class CalculRemise:
    """
    Classe pour gérer le calcul de remise sur un montant donné.
    """

    @staticmethod
    def calculer(montant, remise):
        """
        Calcule le prix après remise.

        :param montant: float, le montant initial de l'article.
        :param remise: float, le pourcentage de remise.
        :return: None, affiche directement le résultat.
        """
        # Vérification des valeurs fournies
        if montant < 0:
            print("Le montant ne peut pas être négatif.")
            return
        if remise < 0 or remise > 100:
            print("La remise doit être comprise entre 0% et 100%.")
            return

        # Calcul du prix après remise
        resultat = montant - montant * (remise / 100)

        # Affichage du résultat formaté
        print(f"Le prix de l'article après la remise est de : {resultat:.2f} €")


# Exemple d'utilisation dans un contexte autonome
if __name__ == "__main__":
    # Exemple d'utilisation de la classe CalculRemise
    montant = float(input("Entrez le montant de l'article : "))
    remise = float(input("Entrez le pourcentage de remise : "))
    CalculRemise.calculer(montant, remise)
