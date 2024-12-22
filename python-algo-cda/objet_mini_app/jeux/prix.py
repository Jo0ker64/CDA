import random  # Importation du module random pour générer des nombres aléatoires

class JeuJustePrix:
    def __init__(self, limite_basse=1, limite_haute=50, max_essais=5):
        """
        Initialise le jeu avec les limites du nombre aléatoire et le nombre maximum d'essais.
        
        :param limite_basse: Limite inférieure du nombre aléatoire (inclus).
        :param limite_haute: Limite supérieure du nombre aléatoire (inclus).
        :param max_essais: Nombre maximum d'essais pour deviner le juste prix.
        """
        # Stocke la limite inférieure pour le nombre à deviner
        self.limite_basse = limite_basse
        # Stocke la limite supérieure pour le nombre à deviner
        self.limite_haute = limite_haute
        # Stocke le nombre maximum d'essais permis
        self.max_essais = max_essais
        # Génère un nombre aléatoire entre limite_basse et limite_haute que le joueur doit deviner
        self.prix = random.randint(self.limite_basse, self.limite_haute)

    def jouer(self):
        """
        Lance le jeu et guide le joueur à travers le processus de devinette.
        """
        # Affiche un message de bienvenue
        print("Bienvenue au Juste Prix !")
        # Informe le joueur des limites du nombre aléatoire
        print(f"Je pense à un nombre entre {self.limite_basse} et {self.limite_haute}.")
        # Informe le joueur du nombre maximum d'essais autorisés
        print(f"Vous avez {self.max_essais} essais pour le deviner.")

        # Boucle pour chaque essai du joueur, allant de 1 à max_essais inclus
        for essai in range(1, self.max_essais + 1):
            # Appelle la méthode pour demander un nombre au joueur pour le devinette actuelle
            guess = self.demander_deviner(essai)
            
            # Vérifie si le joueur a deviné le juste prix
            if self.verifier_deviner(guess, essai):
                # Si le joueur a deviné correctement, termine le jeu
                return
            
            # Si le joueur n'a pas trouvé et qu'il reste des essais, informe du nombre d'essais restants
            if essai < self.max_essais:
                print(f"Il vous reste {self.max_essais - essai} essai(s).")
        
        # Si le joueur n'a pas trouvé le prix après le nombre maximal d'essais, affiche un message de perte
        self.afficher_perdu()

    def demander_deviner(self, essai):
        """
        Demande au joueur de faire une tentative de devinette.
        
        :param essai: Le numéro de l'essai actuel
        :return: La devinette du joueur en tant qu'entier
        """
        while True:
            # Tente d'obtenir un nombre valide de la part du joueur
            try:
                # Demande au joueur d'entrer un nombre pour cet essai
                return int(input(f"Essai {essai}/{self.max_essais} - Devinez le prix : "))
            except ValueError:
                # Si la saisie est invalide, informe le joueur et continue de demander
                print("Veuillez entrer un nombre valide.")

    def verifier_deviner(self, guess, essai):
        """
        Vérifie si le nombre deviné est correct, trop bas ou trop haut.
        
        :param guess: La tentative de devinette de l'utilisateur
        :param essai: Le numéro de l'essai actuel
        :return: True si le joueur a deviné correctement, sinon False
        """
        # Vérifie si la devinette du joueur est inférieure au juste prix
        if guess < self.prix:
            # Indique au joueur que le juste prix est plus élevé
            print("C'est plus !")
        # Vérifie si la devinette du joueur est supérieure au juste prix
        elif guess > self.prix:
            # Indique au joueur que le juste prix est plus bas
            print("C'est moins !")
        else:
            # Si le joueur a trouvé le juste prix, affiche un message de réussite
            print(f"Bravo ! Vous avez trouvé le juste prix en {essai} essai(s).")
            return True  # Retourne True pour indiquer que le jeu est gagné
        return False  # Retourne False pour continuer le jeu

    def afficher_perdu(self):
        """
        Affiche un message si le joueur a utilisé tous ses essais sans deviner le juste prix.
        """
        # Informe le joueur qu'il n'a pas trouvé le juste prix dans le nombre d'essais permis
        print(f"Désolé, vous n'avez pas trouvé le juste prix en {self.max_essais} essais.")
        # Indique au joueur quel était le juste prix
        print(f"Le juste prix était {self.prix}.")

# Point d'entrée du programme
if __name__ == "__main__":
    # Crée une instance de JeuJustePrix et lance le jeu
    jeu = JeuJustePrix()
    jeu.jouer()
