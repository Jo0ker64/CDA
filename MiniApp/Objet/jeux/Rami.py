import random


class Carte:
    """
    Classe représentant une carte individuelle avec sa valeur et sa couleur.
    """
    cartes_unicode = {
        (1, "♥"): "🂱 A♥", (2, "♥"): "🂲 2♥", (3, "♥"): "🂳 3♥", (4, "♥"): "🂴 4♥", (5, "♥"): "🂵 5♥",
        (6, "♥"): "🂶 6♥", (7, "♥"): "🂷 7♥", (8, "♥"): "🂸 8♥", (9, "♥"): "🂹 9♥", (10, "♥"): "🂺 10♥",
        (11, "♥"): "🂻 V♥", (12, "♥"): "🂽 D♥", (13, "♥"): "🂾 R♥",
        (1, "♦"): "🃁 A♦", (2, "♦"): "🃂 2♦", (3, "♦"): "🃃 3♦", (4, "♦"): "🃄 4♦", (5, "♦"): "🃅 5♦",
        (6, "♦"): "🃆 6♦", (7, "♦"): "🃇 7♦", (8, "♦"): "🃈 8♦", (9, "♦"): "🃉 9♦", (10, "♦"): "🃊 10♦",
        (11, "♦"): "🃋 V♦", (12, "♦"): "🃍 D♦", (13, "♦"): "🃎 R♦",
        (1, "♠"): "🂡 A♠", (2, "♠"): "🂢 2♠", (3, "♠"): "🂣 3♠", (4, "♠"): "🂤 4♠", (5, "♠"): "🂥 5♠",
        (6, "♠"): "🂦 6♠", (7, "♠"): "🂧 7♠", (8, "♠"): "🂨 8♠", (9, "♠"): "🂩 9♠", (10, "♠"): "🂪 10♠",
        (11, "♠"): "🂫 V♠", (12, "♠"): "🂭 D♠", (13, "♠"): "🂮 R♠",
        (1, "♣"): "🃑 A♣", (2, "♣"): "🃒 2♣", (3, "♣"): "🃓 3♣", (4, "♣"): "🃔 4♣", (5, "♣"): "🃕 5♣",
        (6, "♣"): "🃖 6♣", (7, "♣"): "🃗 7♣", (8, "♣"): "🃘 8♣", (9, "♣"): "🃙 9♣", (10, "♣"): "🃚 10♣",
        (11, "♣"): "🃛 V♣", (12, "♣"): "🃝 D♣", (13, "♣"): "🃞 R♣",
        (15, "J"): "Joker"
    }

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return Carte.cartes_unicode[(self.valeur, self.couleur)]


class Sabot:
    """
    Classe représentant un sabot contenant toutes les cartes nécessaires.
    """
    def __init__(self):
        self.cartes = []
        self.creer_jeu()

    def creer_jeu(self):
        """
        Crée le jeu de cartes et mélange les cartes.
        """
        for couleur in ["♥", "♦", "♠", "♣"]:
            for valeur in range(1, 14):  # De 1 à 13 (As à Roi)
                self.cartes.append(Carte(valeur, couleur))
        self.cartes.append(Carte(15, "J"))  # Joker
        random.shuffle(self.cartes)

    def tirer_carte(self):
        """
        Tire une carte du sabot.
        """
        return self.cartes.pop()


class Rami:
    """
    Classe principale pour gérer une partie de Rami.
    """
    def __init__(self):
        self.sabot = Sabot()
        self.mains = {"joueur": [], "ordi": []}
        self.pioche = []
        self.defausse = []

        # Distribution initiale
        self.distribuer_cartes()

    def distribuer_cartes(self):
        """
        Distribue les cartes aux joueurs et initialise la défausse et la pioche.
        """
        self.mains["joueur"] = [self.sabot.tirer_carte() for _ in range(15)]
        self.mains["ordi"] = [self.sabot.tirer_carte() for _ in range(14)]
        self.defausse.append(self.sabot.tirer_carte())
        self.pioche = self.sabot.cartes

    def afficher_main(self, joueur):
        """
        Affiche la main du joueur spécifié.
        """
        print(f"\nMain de {joueur} :")
        for i, carte in enumerate(self.mains[joueur], start=1):
            print(f"{i}: {carte}")

    def verifier_combinaison(self, cartes):
        """
        Vérifie si une liste de cartes forme une combinaison valide (suite ou groupe).
        """
        valeurs = sorted([carte.valeur for carte in cartes])
        couleurs = [carte.couleur for carte in cartes]

        # Vérification pour une suite
        if len(set(couleurs)) == 1 and valeurs == list(range(valeurs[0], valeurs[0] + len(cartes))):
            return True

        # Vérification pour un groupe
        if len(set(valeurs)) == 1 and len(set(couleurs)) == len(cartes):
            return True

        return False

    def jouer(self):
        """
        Lance une partie de Rami.
        """
        print("Bienvenue au jeu de Rami !")
        self.afficher_main("joueur")

        while self.mains["joueur"] and self.mains["ordi"]:
            # Tour du joueur
            self.tour_joueur()

            if not self.mains["joueur"]:
                print("Félicitations, vous avez gagné !")
                return

            # Tour de l'ordinateur
            self.tour_ordi()

            if not self.mains["ordi"]:
                print("L'ordinateur a gagné.")
                return

    def tour_joueur(self):
        """
        Gère le tour du joueur.
        """
        print("\n--- Votre Tour ---")
        self.afficher_main("joueur")

        # Piocher une carte
        choix = input("Voulez-vous piocher de la défausse (D) ou de la pioche (P) ? ").upper()
        if choix == "D" and self.defausse:
            carte_piochee = self.defausse.pop()
        else:
            carte_piochee = self.pioche.pop(0)

        print(f"Vous avez pioché : {carte_piochee}")
        self.mains["joueur"].append(carte_piochee)

        # Défausser une carte
        self.afficher_main("joueur")
        index = int(input("Choisissez la carte à défausser : ")) - 1
        carte_defaussee = self.mains["joueur"].pop(index)
        self.defausse.append(carte_defaussee)
        print(f"Vous avez défaussé : {carte_defaussee}")

    def tour_ordi(self):
        """
        Gère le tour de l'ordinateur.
        """
        print("\n--- Tour de l'ordinateur ---")
        if self.pioche:
            self.mains["ordi"].append(self.pioche.pop(0))
        elif self.defausse:
            self.mains["ordi"].append(self.defausse.pop())

        # Défausse aléatoire
        carte_defaussee = self.mains["ordi"].pop(random.randint(0, len(self.mains["ordi"]) - 1))
        self.defausse.append(carte_defaussee)
        print("L'ordinateur a défaussé une carte.")


# Exemple d'utilisation autonome
if __name__ == "__main__":
    jeu = Rami()
    jeu.jouer()
