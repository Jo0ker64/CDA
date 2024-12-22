import random

class ChifoumiSheldon:
    """
    Classe représentant le jeu de Chifoumi Sheldon.
    """

    def __init__(self):
        """
        Initialise les règles du jeu et les choix possibles.
        """
        self.regles = {
            "Pierre": {
                "Ciseaux": "La pierre émousse le ciseau et gagne.",
                "Lézard": "La pierre écrase le lézard et gagne."
            },
            "Feuille": {
                "Pierre": "La feuille enveloppe la pierre et gagne.",
                "Spock": "La feuille discrédite Spock et gagne."
            },
            "Ciseaux": {
                "Feuille": "Le ciseau coupe la feuille et gagne.",
                "Lézard": "Le ciseau décapite le lézard et gagne."
            },
            "Lézard": {
                "Spock": "Le lézard empoisonne Spock et gagne.",
                "Feuille": "Le lézard mange le papier et gagne."
            },
            "Spock": {
                "Ciseaux": "Spock écrase le ciseau et gagne.",
                "Pierre": "Spock vaporise la pierre et gagne."
            }
        }
        self.choix = list(self.regles.keys())  # Liste des choix possibles (Pierre, Feuille, etc.)

    def jouer(self):
        """
        Méthode principale pour jouer à Chifoumi Sheldon.
        """
        print("Bienvenue dans Chifoumi Sheldon !")
        print("Choisissez Pierre, Feuille, Ciseaux, Lézard, ou Spock.")
        print("Tapez 'Q' pour quitter.")

        while True:
            # Demande à Sheldon son choix
            Sheldon = input("Votre choix : ").capitalize()

            # Quitter le jeu si l'utilisateur entre 'Q'
            if Sheldon == 'Q':
                break

            # Vérifie si le choix de Sheldon est valide
            if Sheldon not in self.choix:
                print("Choix invalide, veuillez réessayer.")
                continue

            # Howard choisit aléatoirement
            Howard = random.choice(self.choix)
            print(f"Howard a choisi : {Howard}")

            # Détermine le résultat
            if Sheldon == Howard:
                print("Égalité !")
            elif Howard in self.regles[Sheldon]:
                print("Sheldon gagne !")
                print(self.regles[Sheldon][Howard])
            else:
                print("Sheldon perd !")
                print(self.regles[Howard][Sheldon])

        print("Merci d'avoir joué !")
