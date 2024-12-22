import random  # Importation du module random pour choisir un mot aléatoire

class JeuDuPendu:
    """
    Classe pour gérer le jeu du pendu.
    """

    def __init__(self):
        """
        Initialise les attributs nécessaires pour le jeu.
        """
        # Liste des mots possibles pour le jeu
        self.mots = ["python", "ordinateur", "programmation", "intelligence", "algorithme"]
        # Nombre maximum de tentatives avant de perdre
        self.tentatives_max = 6
        # Choisit un mot aléatoire dans la liste et le met en majuscules
        self.mot_a_deviner = self.choisir_mot()
        # Initialise l'ensemble des lettres trouvées par le joueur
        self.lettres_trouvees = set()
        # Compteur pour le nombre de tentatives du joueur
        self.tentatives = 0
        # Ensemble pour stocker les lettres déjà essayées par le joueur
        self.lettres_essayees = set()

    def choisir_mot(self):
        """
        Choisit un mot aléatoire dans la liste des mots.

        :return: Un mot en majuscules choisi aléatoirement
        """
        return random.choice(self.mots).upper()

    def afficher_mot(self):
        """
        Génère une représentation du mot avec les lettres trouvées et des underscores pour les lettres manquantes.

        :return: Une chaîne de caractères représentant le mot à deviner
        """
        # Affiche les lettres trouvées ou un "_" pour chaque lettre non devinée
        affichage = [lettre if lettre in self.lettres_trouvees else "_" for lettre in self.mot_a_deviner]
        return " ".join(affichage)

    def afficher_pendu(self):
        """
        Affiche l'état graphique du pendu en fonction du nombre de tentatives.
        """
        # Affiche le pendu étape par étape en fonction du nombre de tentatives
        if self.tentatives >= 6:
            print(" ==========Y= ")
        if self.tentatives >= 5:
            print(" ||/       |  ")
        if self.tentatives >= 4:
            print(" ||        0  ")
        if self.tentatives >= 3:
            print(" ||       /|\\ ")
        if self.tentatives >= 2:
            print(" ||       / \\ ")
        if self.tentatives >= 1:                    
            print("/||           ")
        if self.tentatives >= 0:
            print("==============\n")

    def jouer(self):
        """
        Lance le jeu du pendu et guide le joueur à travers les tentatives jusqu'à la victoire ou la défaite.
        """
        # Boucle de jeu qui se termine si le joueur perd ou trouve le mot
        while self.tentatives < self.tentatives_max:
            # Affiche l'état actuel du mot à deviner
            print("\nMot à deviner :", self.afficher_mot())
            # Affiche l'état actuel du pendu
            self.afficher_pendu()
            # Affiche les lettres déjà essayées par le joueur
            print("Lettres essayées :", " ".join(sorted(self.lettres_essayees)))
            # Affiche le nombre d'essais restants
            print("Essais restants :", self.tentatives_max - self.tentatives)

            # Demande une lettre au joueur
            lettre = input("Proposez une lettre : ").upper()

            # Vérifie si la lettre a déjà été essayée
            if lettre in self.lettres_essayees:
                print("Vous avez déjà essayé cette lettre.")
                continue

            # Ajoute la lettre à l'ensemble des lettres essayées
            self.lettres_essayees.add(lettre)

            # Vérifie si la lettre est dans le mot à deviner
            if lettre in self.mot_a_deviner:
                # Ajoute la lettre à l'ensemble des lettres trouvées
                self.lettres_trouvees.add(lettre)
                print("Bonne lettre !")
            else:
                # Incrémente les tentatives si la lettre est incorrecte
                self.tentatives += 1
                print("Mauvaise lettre.")

            # Vérifie si le joueur a trouvé toutes les lettres du mot
            if all(l in self.lettres_trouvees for l in self.mot_a_deviner):
                print("\nFélicitations ! Vous avez deviné le mot :", self.mot_a_deviner)
                break
        else:
            # Si le joueur utilise toutes les tentatives, il perd
            print("\nVous avez perdu ! Le mot était :", self.mot_a_deviner)
            # Affiche l'état final du pendu pour montrer la défaite
            self.afficher_pendu()

# Point d'entrée du programme
if __name__ == "__main__":
    # Crée une instance du jeu du pendu
    jeu = JeuDuPendu()
    # Lance le jeu
    jeu.jouer()
