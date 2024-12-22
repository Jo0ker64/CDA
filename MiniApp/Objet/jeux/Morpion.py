import random


class Morpion:
    """
    Classe représentant le jeu de Morpion.
    """

    def __init__(self):
        """
        Initialise la grille de jeu et le joueur actuel.
        """
        self.grille = [[" " for _ in range(3)] for _ in range(3)]  # Grille 3x3
        self.joueur = "X"  # Le joueur humain commence toujours avec "X"

    def afficher_grille(self):
        """
        Affiche la grille de jeu avec des repères de lignes et colonnes.
        """
        print("    0   1   2 ")
        print("  ------------")
        for i, ligne in enumerate(self.grille):
            print(f"{i} | " + " | ".join(ligne) + " |")
            print("  ------------")

    def verifier_gagnant(self):
        """
        Vérifie si un joueur a gagné.
        :return: bool, True si un joueur a gagné, sinon False.
        """
        for i in range(3):
            # Vérifie les lignes et les colonnes
            if self.grille[i][0] == self.grille[i][1] == self.grille[i][2] != " ":
                return True
            if self.grille[0][i] == self.grille[1][i] == self.grille[2][i] != " ":
                return True

        # Vérifie les diagonales
        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != " ":
            return True
        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != " ":
            return True

        return False

    def coup_ordinateur(self):
        """
        L'ordinateur choisit un emplacement libre de manière aléatoire.
        :return: tuple (ligne, colonne), les coordonnées choisies.
        """
        cases_libres = [(i, j) for i in range(3) for j in range(3) if self.grille[i][j] == " "]
        return random.choice(cases_libres)

    def jouer(self):
        """
        Méthode principale pour jouer au Morpion.
        """
        print("Bienvenue au jeu de Morpion !")
        print("Pour jouer, entrez les coordonnées de votre coup (exemple : 0 1).")

        # Boucle de jeu (maximum 9 tours)
        for tour in range(9):
            self.afficher_grille()

            if self.joueur == "X":
                # Tour du joueur humain
                print(f"Joueur {self.joueur}, entrez votre position (ligne et colonne) : ")
                while True:
                    try:
                        ligne, colonne = map(int, input().split())
                        if ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2:
                            print("Coordonnées hors limites. Entrez des nombres entre 0 et 2.")
                            continue
                        if self.grille[ligne][colonne] != " ":
                            print("Position déjà occupée, essayez à nouveau.")
                            continue
                        break
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer deux chiffres séparés par un espace, par exemple : 0 1.")

                # Place le symbole du joueur sur la grille
                self.grille[ligne][colonne] = self.joueur
            else:
                # Tour de l'ordinateur
                print("Tour de l'ordinateur...")
                ligne, colonne = self.coup_ordinateur()
                self.grille[ligne][colonne] = self.joueur
                print(f"L'ordinateur joue en position ({ligne}, {colonne})")

            # Vérifie si le joueur actuel a gagné
            if self.verifier_gagnant():
                self.afficher_grille()
                print(f"Le joueur {self.joueur} a gagné !" if self.joueur == "X" else "L'ordinateur a gagné !")
                return

            # Change de joueur
            self.joueur = "O" if self.joueur == "X" else "X"

        # Si aucun joueur n'a gagné après 9 tours
        self.afficher_grille()
        print("Match nul !")


# Exemple d'utilisation autonome
if __name__ == "__main__":
    jeu = Morpion()  # Crée une instance du jeu
    jeu.jouer()  # Lance le jeu
