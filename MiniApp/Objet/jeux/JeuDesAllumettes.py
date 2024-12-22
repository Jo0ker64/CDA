import random  # Pour les choix aléatoires de l'ordinateur

class JeuDesAllumettes:
    """
    Classe représentant le jeu des allumettes.
    """

    def __init__(self, total_allumettes=20):
        """
        Initialise le jeu avec le nombre total d'allumettes.
        :param total_allumettes: int, nombre initial d'allumettes (par défaut : 20).
        """
        self.total_allumettes = total_allumettes  # Nombre initial d'allumettes

    def afficher_regles(self):
        """
        Affiche les règles du jeu des allumettes.
        """
        print("Bienvenue au Jeu des Allumettes !")
        print("Règles du jeu :")
        print("- Il y a 20 allumettes sur la table.")
        print("- Vous et l'ordinateur jouez chacun votre tour.")
        print("- À chaque tour, vous pouvez retirer 1, 2 ou 3 allumettes.")
        print("- Le joueur qui est obligé de prendre la dernière allumette perd la partie.")
        print("Essayez d'éviter de prendre la dernière allumette pour gagner !\n")

    def joueur_retirer(self):
        """
        Gère le tour du joueur.
        Retourne le nombre d'allumettes retirées par le joueur.
        """
        while True:
            try:
                joueur_retrait = int(input("Combien d'allumettes voulez-vous retirer ? (1, 2 ou 3) : "))
                if joueur_retrait in [1, 2, 3] and joueur_retrait <= self.total_allumettes:
                    return joueur_retrait
                else:
                    print("Choix invalide. Essayez à nouveau.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")  # Gestion des erreurs de saisie

    def ordinateur_retirer(self):
        """
        Gère le tour de l'ordinateur.
        Retourne le nombre d'allumettes retirées par l'ordinateur.
        """
        return random.randint(1, min(3, self.total_allumettes))

    def jouer(self):
        """
        Lance le jeu des allumettes et gère la boucle principale.
        """
        self.afficher_regles()  # Affiche les règles au début du jeu
        while self.total_allumettes > 0:
            print(f"\nAllumettes restantes : {self.total_allumettes}")
            joueur_retrait = self.joueur_retirer()
            self.total_allumettes -= joueur_retrait
            if self.total_allumettes == 0:
                print("Vous avez pris la dernière allumette. Vous avez perdu !")
                break
            ordi_retrait = self.ordinateur_retirer()
            print(f"L'ordinateur retire {ordi_retrait} allumette(s).")
            self.total_allumettes -= ordi_retrait
            if self.total_allumettes == 0:
                print("L'ordinateur a pris la dernière allumette. Vous avez gagné !")
                break
