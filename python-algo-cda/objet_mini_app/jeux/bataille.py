import random

def creer_grille():
    """Crée et retourne une grille vide de 5x5 pour le jeu."""
    return [["~" for _ in range(5)] for _ in range(5)]

def placer_navire(grille):
    """Place un navire de 3 cases de manière aléatoire sur la grille."""
    # Choisit aléatoirement l'orientation du navire : horizontal ou vertical
    orientation = random.choice(["horizontal", "vertical"])
    
    # Place le navire en fonction de son orientation
    if orientation == "horizontal":
        # Place le navire horizontalement dans une ligne aléatoire
        ligne = random.randint(0, 4)
        colonne = random.randint(0, 2)  # Limite pour qu'il reste dans la grille 5x5
        for i in range(3):
            grille[ligne][colonne + i] = "N"  # Place chaque partie du navire
    else:
        # Place le navire verticalement dans une colonne aléatoire
        ligne = random.randint(0, 2)  # Limite pour qu'il reste dans la grille 5x5
        colonne = random.randint(0, 4)
        for i in range(3):
            grille[ligne + i][colonne] = "N"  # Place chaque partie du navire
    return grille

def afficher_grille(grille, masque=False):
    """Affiche la grille. Si masque=True, cache les navires non touchés."""
    for ligne in grille:
        for case in ligne:
            # Affiche "~" à la place des navires cachés si masque est activé
            if masque and case == "N":
                print("~", end=" ")
            else:
                print(case, end=" ")
        print()  # Nouvelle ligne après chaque ligne de la grille
    print()  # Espacement après la grille

def bataille_navale():
    # Initialise la grille et place le navire
    grille = creer_grille()
    grille = placer_navire(grille)
    tentatives = 10  # Nombre de tentatives autorisées pour le joueur

    # Affiche les règles du jeu
    print("Bienvenue dans la Bataille Navale Simplifiée !")
    print("Règles du jeu :")
    print("- Vous jouez sur une grille 5x5.")
    print("- Un navire de 3 cases est placé quelque part sur la grille.")
    print("- Vous devez deviner les positions du navire en entrant les coordonnées.")
    print("- Si vous touchez toutes les cases du navire, vous gagnez.")
    print("- Vous avez 10 tentatives pour trouver le navire.")
    print("Bon courage !\n")

    # Affiche la grille masquée au joueur
    afficher_grille(grille, masque=True)

    # Boucle de jeu principale
    while tentatives > 0:
        # Demande au joueur d'entrer les coordonnées de tir
        try:
            ligne = int(input("Entrez la ligne (0 à 4) : "))
            colonne = int(input("Entrez la colonne (0 à 4) : "))
            
            # Vérifie si les coordonnées sont valides
            if not (0 <= ligne <= 4 and 0 <= colonne <= 4):
                print("Coordonnées invalides. Essayez à nouveau.")
                continue
        except ValueError:
            print("Veuillez entrer un nombre valide.")  # Gestion des erreurs de saisie
            continue

        # Vérifie si le tir touche le navire
        if grille[ligne][colonne] == "N":
            print("Touché !")
            grille[ligne][colonne] = "X"  # Marque la case comme touchée
        elif grille[ligne][colonne] == "~":
            print("Manqué.")
            grille[ligne][colonne] = "O"  # Marque la case comme manquée
        else:
            print("Vous avez déjà tiré ici.")  # Si le joueur vise une case déjà touchée ou manquée

        # Diminue le nombre de tentatives restantes
        tentatives -= 1
        afficher_grille(grille, masque=True)  # Affiche la grille mise à jour

        # Vérifie si toutes les parties du navire ont été touchées
        if all(cell != "N" for row in grille for cell in row):
            print("Félicitations ! Vous avez coulé le navire.")
            break  # Fin du jeu si le navire est coulé
    else:
        # Si les tentatives sont épuisées sans avoir coulé le navire
        print("Vous avez épuisé vos tentatives. Partie terminée !")
        print("Voici la position du navire :")
        afficher_grille(grille)  # Affiche la grille complète avec la position du navire

# Point d'entrée du programme
if __name__ == "__main__":
    bataille_navale()  # Lancement de la Bataille Navale Simplifiée
