import random

class JeuDuPendu:
    """
    Classe représentant le jeu du pendu.
    """

    def __init__(self):
        """
        Initialise les paramètres du jeu.
        """
        self.mots = ["python", "ordinateur", "programmation", "intelligence", "algorithme"]  # Liste des mots
        self.mot_a_deviner = self.choisir_mot()  # Mot choisi pour le jeu
        self.lettres_trouvees = set()  # Lettres déjà trouvées
        self.tentatives = 0  # Nombre de tentatives effectuées
        self.lettres_essayees = set()  # Lettres déjà essayées
        self.max_tentatives = 6  # Nombre maximum de tentatives autorisées

    def choisir_mot(self):
        """
        Sélectionne un mot aléatoire dans la liste.

        :return: str, le mot choisi en majuscules.
        """
        return random.choice(self.mots).upper()

    def afficher_mot(self):
        """
        Affiche le mot avec les lettres trouvées et des underscores pour les lettres non devinées.

        :return: str, le mot avec les lettres trouvées et des underscores.
        """
        return " ".join([lettre if lettre in self.lettres_trouvees else "_" for lettre in self.mot_a_deviner])

    def afficher_pendu(self):
        """
        Affiche le dessin du pendu en fonction du nombre de tentatives.
        """
        if self.tentatives >= 6:
            print(" ==========Y= ")
        if self.tentatives >= 5:
            print(" ||/       |  ")
        if self.tentatives >= 4:
            print(" ||        0  ")
        if self.tentatives >= 3:
            print(r" ||       /|\ ")
        if self.tentatives >= 2:
            print(r" ||       / \ ")
        if self.tentatives >= 1:                    
            print("/||           ")
        if self.tentatives >= 0:
            print("==============\n")

    def jouer(self):
        """
        Méthode principale pour jouer au jeu du pendu.
        """
        print("Bienvenue au Jeu du Pendu !")

        while self.tentatives < self.max_tentatives:
            # Affichage de l'état actuel du jeu
            print("\nMot à deviner :", self.afficher_mot())
            self.afficher_pendu()
            print("Lettres essayées :", " ".join(sorted(self.lettres_essayees)))
            print("Essais restants :", self.max_tentatives - self.tentatives)

            # Demande une lettre au joueur
            lettre = input("Proposez une lettre : ").upper()

            # Vérifie si la lettre a déjà été essayée
            if lettre in self.lettres_essayees:
                print("Vous avez déjà essayé cette lettre.")
                continue

            # Ajoute la lettre à la liste des lettres essayées
            self.lettres_essayees.add(lettre)

            # Vérifie si la lettre est dans le mot
            if lettre in self.mot_a_deviner:
                self.lettres_trouvees.add(lettre)
                print("Bonne lettre !")
            else:
                self.tentatives += 1
                print("Mauvaise lettre.")

            # Vérifie si toutes les lettres du mot ont été trouvées
            if all(l in self.lettres_trouvees for l in self.mot_a_deviner):
                print("\nFélicitations ! Vous avez deviné le mot :", self.mot_a_deviner)
                return

        # Si le joueur a épuisé toutes ses tentatives
        print("\nVous avez perdu ! Le mot était :", self.mot_a_deviner)
        self.afficher_pendu()  # Affiche le pendu complet

# Exemple d'utilisation autonome
if __name__ == "__main__":
    jeu = JeuDuPendu()  # Crée une instance du jeu du pendu
    jeu.jouer()  # Lance le jeu
