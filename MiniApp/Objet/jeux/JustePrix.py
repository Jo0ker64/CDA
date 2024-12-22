import random

class JustePrix:
    """
    Classe pour gérer le jeu du Juste Prix.
    """

    def __init__(self, limite_basse=1, limite_haute=50, max_essais=5):
        """
        Initialise les paramètres du jeu.

        :param limite_basse: int, la limite basse pour le nombre à deviner (par défaut : 1).
        :param limite_haute: int, la limite haute pour le nombre à deviner (par défaut : 50).
        :param max_essais: int, le nombre maximum d'essais autorisés (par défaut : 5).
        """
        self.limite_basse = limite_basse  # Limite basse pour le nombre à deviner
        self.limite_haute = limite_haute  # Limite haute pour le nombre à deviner
        self.max_essais = max_essais  # Nombre maximum d'essais
        self.prix = random.randint(self.limite_basse, self.limite_haute)  # Nombre aléatoire à deviner

    def jouer(self):
        """
        Méthode principale pour jouer au Juste Prix.
        """
        print(f"Bienvenue au Juste Prix !")
        print(f"Je pense à un nombre entre {self.limite_basse} et {self.limite_haute}.")
        print(f"Vous avez {self.max_essais} essais pour le deviner.")

        for essai in range(1, self.max_essais + 1):
            try:
                # Demander au joueur de deviner le prix
                guess = int(input(f"Essai {essai}/{self.max_essais} - Devinez le prix : "))
            except ValueError:
                # Gestion des erreurs si l'entrée n'est pas un nombre valide
                print("Veuillez entrer un nombre valide.")
                continue

            # Vérifier si la tentative est correcte, trop basse ou trop haute
            if guess < self.prix:
                print("C'est plus !")
            elif guess > self.prix:
                print("C'est moins !")
            else:
                print(f"Bravo ! Vous avez trouvé le juste prix en {essai} essai(s).")
                return  # Terminer la méthode si le joueur a trouvé

            # Informer le joueur du nombre d'essais restants
            if essai < self.max_essais:
                print(f"Il vous reste {self.max_essais - essai} essai(s).")

        # Si le joueur n'a pas trouvé après tous les essais
        print(f"Désolé, vous n'avez pas trouvé le juste prix en {self.max_essais} essais.")
        print(f"Le juste prix était {self.prix}.")

# Exemple d'utilisation autonome
if __name__ == "__main__":
    jeu = JustePrix()  # Crée une instance de la classe JustePrix
    jeu.jouer()  # Lance le jeu
