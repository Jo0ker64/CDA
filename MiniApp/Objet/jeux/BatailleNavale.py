import random


class BatailleNavale:
    """
    Classe représentant le jeu de Bataille Navale Simplifiée.
    """

    def __init__(self):
        """
        Initialise une grille vide de 5x5 et place un navire de 3 cases.
        """
        self.grille = self.creer_grille()
        self.tentatives = 10  # Nombre de tentatives autorisées pour le joueur
        self.placer_navire()

    def creer_grille(self):
        """
        Crée et retourne une grille vide de 5x5 pour le jeu.
        :return: list[list[str]], grille vide.
        """
        return [["~" for _ in range(5)] for _ in range(5)]

    def placer_navire(self):
        """
        Place un navire de 3 cases de manière aléatoire sur la grille.
        """
        orientation = random.choice(["horizontal", "vertical"])
        if orientation == "horizontal":
            ligne = random.randint(0, 4)
            colonne = random.randint(0, 2)
            for i in range(3):
                self.grille[ligne][colonne + i] = "N"
        else:
            ligne = random.randint(0, 2)
            colonne = random.randint(0, 4)
            for i in range(3):
                self.grille[ligne + i][colonne] = "N"

    def afficher_grille(self, masque=False):
        """
        Affiche la grille avec des repères de colonnes (A-E) et de lignes (1-5).
        Si masque=True, cache les navires non touchés.
        :param masque: bool, masque les navires si True.
        """
        # Affichage des repères des colonnes
        print("    " + "   ".join("A B C D E".split()))
        print("  " + "-" * 20)  # Ligne de séparation

        # Affichage des lignes avec repères
        for i, ligne in enumerate(self.grille):
            ligne_affichee = [cell if not masque or cell != "N" else "~" for cell in ligne]
            print(f"{i + 1} | " + " | ".join(ligne_affichee) + " |")
            print("  " + "-" * 20)

    def jouer(self):
        """
        Lance le jeu de Bataille Navale Simplifiée.
        """
        print("Bienvenue dans la Bataille Navale Simplifiée !")
        print("Règles du jeu :")
        print("- Vous jouez sur une grille 5x5.")
        print("- Les colonnes sont marquées par des lettres (A-E) et les lignes par des chiffres (1-5).")
        print("- Un navire de 3 cases est placé quelque part sur la grille.")
        print("- Vous devez deviner les positions du navire en entrant les coordonnées.")
        print("- Si vous touchez toutes les cases du navire, vous gagnez.")
        print("- Vous avez 10 tentatives pour trouver le navire.")
        print("Bon courage !\n")

        self.afficher_grille(masque=True)

        while self.tentatives > 0:
            try:
                # Demande au joueur les coordonnées du tir
                entree = input("Entrez les coordonnées (ex: A1) : ").strip().upper()
                if len(entree) != 2 or not entree[0].isalpha() or not entree[1].isdigit():
                    print("Format invalide. Utilisez une lettre (A-E) suivie d'un chiffre (1-5).")
                    continue

                colonne = ord(entree[0]) - ord('A')  # Convertit la lettre en index
                ligne = int(entree[1]) - 1  # Convertit le chiffre en index

                # Vérifie si les coordonnées sont valides
                if not (0 <= ligne < 5 and 0 <= colonne < 5):
                    print("Coordonnées hors limites. Essayez à nouveau.")
                    continue
            except ValueError:
                print("Erreur de saisie. Veuillez réessayer.")
                continue

            # Résultat du tir
            if self.grille[ligne][colonne] == "N":
                print("Touché !")
                self.grille[ligne][colonne] = "X"  # Marque la case comme touchée
            elif self.grille[ligne][colonne] == "~":
                print("Manqué.")
                self.grille[ligne][colonne] = "O"  # Marque la case comme manquée
            else:
                print("Vous avez déjà tiré ici.")  # Case déjà visée

            # Réduit les tentatives restantes
            self.tentatives -= 1
            self.afficher_grille(masque=True)

            # Vérifie si toutes les parties du navire ont été touchées
            if all(cell != "N" for row in self.grille for cell in row):
                print("Félicitations ! Vous avez coulé le navire.")
                return

        # Partie terminée, le joueur a perdu
        print("Vous avez épuisé vos tentatives. Partie terminée !")
        print("Voici la position du navire :")
        self.afficher_grille()  # Affiche la grille complète


# Exemple d'utilisation autonome
if __name__ == "__main__":
    jeu = BatailleNavale()  # Crée une instance du jeu
    jeu.jouer()  # Lance le jeu
