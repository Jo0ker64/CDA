# Importe le module random pour générer des nombres aléatoires
import random

# Définit la classe Case qui représente une case individuelle du jeu
class Case:
    # Initialise une nouvelle instance de Case
    def __init__(self):
        # Indique si la case contient une mine (False par défaut)
        self.mine = False
        # Indique si la case a été révélée (False par défaut)
        self.visible = False
        # Nombre de mines dans les cases adjacentes (0 par défaut)
        self.nb_mines_voisines = 0
        # Indique si la case a été marquée par le joueur (False par défaut)
        self.marquee = False

# Définit la classe principale Demineur qui gère le jeu
class Demineur:
    # Initialise une nouvelle instance de Demineur
    def __init__(self, largeur, hauteur, nb_mines):
        # Définit la largeur de la grille
        self.largeur = largeur
        # Définit la hauteur de la grille
        self.hauteur = hauteur
        # Définit le nombre total de mines
        self.nb_mines = nb_mines
        # Crée la grille de jeu comme une liste 2D de Cases
        self.grille = [[Case() for _ in range(largeur)] for _ in range(hauteur)]
        # Indique si la partie est terminée (False au début)
        self.partie_terminee = False
        # Indique si le joueur a gagné (False au début)
        self.victoire = False
        # Place les mines sur la grille
        self.placer_mines()
        # Calcule le nombre de mines voisines pour chaque case
        self.calculer_nombres()

    # Méthode pour placer aléatoirement les mines sur la grille
    def placer_mines(self):
        # Initialise le compteur de mines placées
        mines_placees = 0
        # Continue jusqu'à ce que toutes les mines soient placées
        while mines_placees < self.nb_mines:
            # Génère des coordonnées aléatoires
            x, y = random.randint(0, self.largeur-1), random.randint(0, self.hauteur-1)
            # Si la case n'a pas déjà une mine, place une mine
            if not self.grille[y][x].mine:
                self.grille[y][x].mine = True
                mines_placees += 1

    # Méthode pour calculer le nombre de mines voisines pour chaque case
    def calculer_nombres(self):
        # Parcourt chaque case de la grille
        for y in range(self.hauteur):
            for x in range(self.largeur):
                # Si la case n'est pas une mine, calcule le nombre de mines voisines
                if not self.grille[y][x].mine:
                    self.grille[y][x].nb_mines_voisines = self.compter_mines_voisines(x, y)

    # Méthode pour compter le nombre de mines dans les cases adjacentes
    def compter_mines_voisines(self, x, y):
        # Initialise le compteur
        count = 0
        # Vérifie les 8 cases adjacentes
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                # Vérifie si la case adjacente est dans la grille et contient une mine
                if 0 <= nx < self.largeur and 0 <= ny < self.hauteur and self.grille[ny][nx].mine:
                    count += 1
        # Retourne le nombre de mines voisines
        return count

    # Méthode pour découvrir une case
    def decouvrir(self, x, y):
        # Si la case est déjà visible ou marquée, ne fait rien
        if self.grille[y][x].visible or self.grille[y][x].marquee:
            return
        # Rend la case visible
        self.grille[y][x].visible = True
        # Si c'est une mine, termine la partie
        if self.grille[y][x].mine:
            self.partie_terminee = True
            return
        # Si la case n'a pas de mines voisines, découvre récursivement les cases adjacentes
        if self.grille[y][x].nb_mines_voisines == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.largeur and 0 <= ny < self.hauteur:
                        self.decouvrir(nx, ny)
        # Vérifie si le joueur a gagné
        self.verifier_victoire()

    # Méthode pour marquer ou démarquer une case
    def marquer(self, x, y):
        # Inverse l'état de marquage si la case n'est pas visible
        if not self.grille[y][x].visible:
            self.grille[y][x].marquee = not self.grille[y][x].marquee

    # Méthode pour vérifier si le joueur a gagné
    def verifier_victoire(self):
        # Parcourt toutes les cases
        for y in range(self.hauteur):
            for x in range(self.largeur):
                # Si une case non-minée n'est pas visible, le jeu continue
                if not self.grille[y][x].mine and not self.grille[y][x].visible:
                    return
        # Si toutes les cases non-minées sont visibles, le joueur gagne
        self.victoire = True
        self.partie_terminee = True

    # Méthode pour afficher la grille
    def afficher(self):
        # Affiche l'en-tête des colonnes (A, B, C, ...)
        print("  ", end="")
        for x in range(self.largeur):
            print(chr(65 + x), end=" ")
        print()
        # Affiche la grille avec les numéros de ligne
        for y in range(self.hauteur):
            print(f"{y+1:2d}", end=" ")  # Numéro de ligne
            for x in range(self.largeur):
                case = self.grille[y][x]
                # Affiche le contenu de la case selon son état
                if case.visible:
                    if case.mine:
                        print("*", end=" ")
                    elif case.nb_mines_voisines > 0:
                        print(case.nb_mines_voisines, end=" ")
                    else:
                        print(".", end=" ")
                elif case.marquee:
                    print("F", end=" ")
                else:
                    print("#", end=" ")
            print()

# Fonction principale pour jouer au jeu
def démineur():
    # Initialise le jeu
    jeu = Demineur(10, 10, 10)
    
    # Boucle principale du jeu
    while not jeu.partie_terminee:
        # Affiche la grille
        jeu.afficher()
        # Demande une action au joueur
        action = input("Entrez votre action (d A1 pour découvrir, m A1 pour marquer): ").split()
        
        # Vérifie la validité de l'action
        if len(action) != 2:
            print("Action invalide. Réessayez.")
            continue
        
        # Sépare la commande et les coordonnées
        commande, coords = action
        # Vérifie le format des coordonnées
        if len(coords) < 2 or not coords[0].isalpha() or not coords[1:].isdigit():
            print("Coordonnées invalides. Utilisez le format 'A1'.")
            continue

        # Convertit les coordonnées en indices de grille
        x = ord(coords[0].upper()) - ord('A')
        y = int(coords[1:]) - 1

        # Vérifie si les coordonnées sont dans les limites
        if x < 0 or x >= jeu.largeur or y < 0 or y >= jeu.hauteur:
            print("Coordonnées hors limites.")
            continue
        
        # Exécute l'action demandée
        if commande == 'd':
            jeu.decouvrir(x, y)
        elif commande == 'm':
            jeu.marquer(x, y)
        else:
            print("Commande invalide. Utilisez 'd' pour découvrir ou 'm' pour marquer.")

    # Affiche la grille finale
    jeu.afficher()
    # Affiche le résultat du jeu
    if jeu.victoire:
        print("Félicitations ! Vous avez gagné !")
    else:
        print("Boom ! Vous avez perdu.")

# Point d'entrée du programme
if __name__ == "__main__":
    # Lance le jeu
    démineur()
