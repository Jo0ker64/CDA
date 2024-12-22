import random

# Fonction pour afficher la grille de jeu avec repères de lignes et colonnes
def afficher_grille(grille):
    # Affiche les en-têtes de colonnes
    print("    0   1   2 ")
    print("  ------------")
    # Parcourt chaque ligne de la grille avec un index pour les repères de ligne
    for i, ligne in enumerate(grille):
        # Affiche le numéro de la ligne et les cases de la ligne séparées par des barres verticales
        print(f"{i} | " + " | ".join(ligne) + " |")
        # Affiche une ligne de séparation pour distinguer les lignes de la grille
        print("  ------------")

# Fonction pour vérifier si un joueur a gagné
def verifier_gagnant(grille):
    # Vérifie les lignes et les colonnes
    for i in range(3):
        # Vérifie si toutes les cases de la ligne i sont identiques et non vides
        if grille[i][0] == grille[i][1] == grille[i][2] != " ":
            return True
        # Vérifie si toutes les cases de la colonne i sont identiques et non vides
        if grille[0][i] == grille[1][i] == grille[2][i] != " ":
            return True
    # Vérifie la diagonale principale
    if grille[0][0] == grille[1][1] == grille[2][2] != " ":
        return True
    # Vérifie la diagonale secondaire
    if grille[0][2] == grille[1][1] == grille[2][0] != " ":
        return True
    # Si aucune condition de victoire n'est remplie, retourne False
    return False

# Fonction pour que l'ordinateur joue de manière aléatoire
def coup_ordinateur(grille):
    """L'ordinateur choisit un emplacement libre de manière aléatoire."""
    cases_libres = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == " "]
    return random.choice(cases_libres)

# Fonction principale du jeu de Morpion
def morpion():
    # Initialise la grille de jeu avec des cases vides (" ")
    grille = [[" " for _ in range(3)] for _ in range(3)]
    joueur = "X"  # Le joueur humain commence toujours avec "X"

    # Boucle de 9 tours maximum (nombre de cases)
    for tour in range(9):
        # Affiche la grille de jeu actuelle avec repères
        afficher_grille(grille)

        if joueur == "X":
            # Tour du joueur humain
            print(f"Joueur {joueur}, entrez votre position (ligne et colonne) : ")
            
            while True:
                try:
                    # Récupère les coordonnées entrées par le joueur et les convertit en entiers
                    ligne, colonne = map(int, input().split())
                    # Vérifie que les coordonnées sont dans les limites de la grille
                    if ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2:
                        print("Coordonnées hors limites. Entrez des nombres entre 0 et 2.")
                        continue
                    # Vérifie si la position est déjà occupée
                    if grille[ligne][colonne] != " ":
                        print("Position déjà occupée, essayez à nouveau.")
                        continue
                    # Si l'entrée est valide, on sort de la boucle
                    break
                except ValueError:
                    print("Entrée invalide. Veuillez entrer deux chiffres séparés par un espace, par exemple : 0 1.")

            # Place le symbole du joueur sur la grille
            grille[ligne][colonne] = joueur

        else:
            # Tour de l'ordinateur
            print("Tour de l'ordinateur...")
            ligne, colonne = coup_ordinateur(grille)
            grille[ligne][colonne] = joueur
            print(f"L'ordinateur joue en position ({ligne}, {colonne})")

        # Vérifie si le joueur actuel a gagné après son coup
        if verifier_gagnant(grille):
            afficher_grille(grille)
            print(f"Le joueur {joueur} a gagné !" if joueur == "X" else "L'ordinateur a gagné !")
            return

        # Change de joueur : X devient O, et O devient X
        joueur = "O" if joueur == "X" else "X"

    # Si aucun joueur n'a gagné après 9 tours, affiche un match nul
    afficher_grille(grille)
    print("Match nul !")

# Point d'entrée du programme
if __name__ == "__main__":
    morpion()
