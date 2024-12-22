import random


class Mastermind:
    """
    Classe représentant le jeu du Mastermind.
    """

    def __init__(self, essais_max=10):
        """
        Initialise le jeu avec les paramètres de base.
        :param essais_max: int, le nombre maximal d'essais.
        """
        self.combinaison_secrete = self.generer_combinaison()
        self.essais_max = essais_max

    @staticmethod
    def generer_combinaison():
        """
        Génère une combinaison secrète de 4 chiffres entre 1 et 6.
        :return: list, la combinaison secrète.
        """
        return [random.randint(1, 6) for _ in range(4)]

    @staticmethod
    def evaluer_proposition(proposition, combinaison_secrete):
        """
        Évalue la proposition du joueur en fonction de la combinaison secrète
        et retourne les pions noirs et blancs.
        :param proposition: list, la proposition du joueur.
        :param combinaison_secrete: list, la combinaison secrète.
        :return: tuple, (noirs, blancs).
        """
        noirs = 0  # Chiffres corrects et bien placés
        blancs = 0  # Chiffres corrects mais mal placés

        # Création de copies pour éviter de modifier les listes d'origine
        combinaison_secrete_copy = combinaison_secrete[:]
        proposition_copy = proposition[:]

        # Vérification des pions noirs
        for i in range(4):
            if proposition[i] == combinaison_secrete_copy[i]:
                noirs += 1
                combinaison_secrete_copy[i] = proposition_copy[i] = None

        # Vérification des pions blancs
        for i in range(4):
            if proposition_copy[i] is not None and proposition_copy[i] in combinaison_secrete_copy:
                blancs += 1
                combinaison_secrete_copy[combinaison_secrete_copy.index(proposition_copy[i])] = None

        return noirs, blancs

    def jouer(self):
        """
        Méthode principale pour lancer le jeu.
        """
        print("Bienvenue au Mastermind ! Devinez la combinaison de 4 chiffres entre 1 et 6.")
        print("Un pion noir signifie qu'un chiffre est correct et bien placé.")
        print("Un pion blanc signifie qu'un chiffre est correct mais mal placé.")

        # Boucle pour les essais
        for essai in range(self.essais_max):
            # Demande au joueur de saisir une combinaison de 4 chiffres
            proposition = input(f"\nEssai {essai + 1}/{self.essais_max} : Entrez votre combinaison de 4 chiffres : ")

            try:
                # Convertit l'entrée en une liste d'entiers
                proposition = list(map(int, proposition.split()))
            except ValueError:
                print("Entrée invalide ! Assurez-vous d'entrer 4 chiffres entre 1 et 6.")
                continue

            # Vérifie la validité de l'entrée
            if len(proposition) != 4 or any(chiffre < 1 or chiffre > 6 for chiffre in proposition):
                print("Entrée invalide ! Assurez-vous d'entrer 4 chiffres entre 1 et 6.")
                continue

            # Évalue la proposition
            noirs, blancs = self.evaluer_proposition(proposition, self.combinaison_secrete)
            print(f"Résultat : {noirs} pion(s) noir(s), {blancs} pion(s) blanc(s)")

            # Vérifie si le joueur a gagné
            if noirs == 4:
                print("Félicitations ! Vous avez deviné la combinaison secrète.")
                return

        # Si le joueur n'a pas trouvé, affiche la combinaison secrète
        print(f"Dommage ! Vous avez épuisé vos essais. La combinaison secrète était : {self.combinaison_secrete}")


# Exemple d'utilisation autonome
if __name__ == "__main__":
    jeu = Mastermind()  # Crée une instance du jeu
    jeu.jouer()  # Lance le jeu
