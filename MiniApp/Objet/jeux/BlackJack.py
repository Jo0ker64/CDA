import random

class Carte:
    """
    Classe représentant une carte individuelle.
    """
    cartes_unicode = {
        ("A", "♥"): "🂱 A♥", ("2", "♥"): "🂲 2♥", ("3", "♥"): "🂳 3♥", ("4", "♥"): "🂴 4♥", ("5", "♥"): "🂵 5♥",
        ("6", "♥"): "🂶 6♥", ("7", "♥"): "🂷 7♥", ("8", "♥"): "🂸 8♥", ("9", "♥"): "🂹 9♥", ("10", "♥"): "🂺 10♥",
        ("V", "♥"): "🂻 V♥", ("D", "♥"): "🂽 D♥", ("R", "♥"): "🂾 R♥",
        ("A", "♦"): "🃁 A♦", ("2", "♦"): "🃂 2♦", ("3", "♦"): "🃃 3♦", ("4", "♦"): "🃄 4♦", ("5", "♦"): "🃅 5♦",
        ("6", "♦"): "🃆 6♦", ("7", "♦"): "🃇 7♦", ("8", "♦"): "🃈 8♦", ("9", "♦"): "🃉 9♦", ("10", "♦"): "🃊 10♦",
        ("V", "♦"): "🃋 V♦", ("D", "♦"): "🃍 D♦", ("R", "♦"): "🃎 R♦",
        ("A", "♠"): "🂡 A♠", ("2", "♠"): "🂢 2♠", ("3", "♠"): "🂣 3♠", ("4", "♠"): "🂤 4♠", ("5", "♠"): "🂥 5♠",
        ("6", "♠"): "🂦 6♠", ("7", "♠"): "🂧 7♠", ("8", "♠"): "🂨 8♠", ("9", "♠"): "🂩 9♠", ("10", "♠"): "🂪 10♠",
        ("V", "♠"): "🂫 V♠", ("D", "♠"): "🂭 D♠", ("R", "♠"): "🂮 R♠",
        ("A", "♣"): "🃑 A♣", ("2", "♣"): "🃒 2♣", ("3", "♣"): "🃓 3♣", ("4", "♣"): "🃔 4♣", ("5", "♣"): "🃕 5♣",
        ("6", "♣"): "🃖 6♣", ("7", "♣"): "🃗 7♣", ("8", "♣"): "🃘 8♣", ("9", "♣"): "🃙 9♣", ("10", "♣"): "🃚 10♣",
        ("V", "♣"): "🃛 V♣", ("D", "♣"): "🃝 D♣", ("R", "♣"): "🃞 R♣"
    }

    def __init__(self, valeur, couleur, points):
        self.valeur = valeur
        self.couleur = couleur
        self.points = points

    def __str__(self):
        return Carte.cartes_unicode[(self.valeur, self.couleur)]


class Sabot:
    """
    Classe représentant un sabot de cartes (4 jeux de 52 cartes).
    """
    def __init__(self):
        self.cartes = []
        self.creer_sabot()

    def creer_sabot(self):
        """
        Crée un sabot de cartes en ajoutant 4 jeux de 52 cartes.
        """
        valeurs = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "V": 10, "D": 10, "R": 10, "A": 11
        }
        couleurs = ["♥", "♦", "♠", "♣"]

        for _ in range(4):  # 4 jeux de cartes
            for couleur in couleurs:
                for valeur, points in valeurs.items():
                    self.cartes.append(Carte(valeur, couleur, points))

        random.shuffle(self.cartes)

    def tirer_carte(self):
        """
        Tire une carte du sabot.
        """
        return self.cartes.pop()


class BlackJack:
    """
    Classe principale pour gérer une partie de Blackjack.
    """
    def __init__(self):
        self.sabot = Sabot()
        self.main_joueur = []
        self.main_croupier = []

    def calculer_valeur_main(self, main):
        """
        Calcule la valeur totale d'une main.
        """
        valeur_totale = sum(carte.points for carte in main)
        nombre_as = sum(1 for carte in main if carte.valeur == "A")

        # Ajuster les As si la valeur totale dépasse 21
        while valeur_totale > 21 and nombre_as > 0:
            valeur_totale -= 10
            nombre_as -= 1

        return valeur_totale

    def afficher_main(self, joueur, main):
        """
        Affiche les cartes et la valeur totale d'une main.
        """
        print(f"\nMain de {joueur} :")
        for carte in main:
            print(f"  - {carte}")
        print(f"Valeur totale: {self.calculer_valeur_main(main)}")

    def jouer(self):
        """
        Gère une partie complète de Blackjack.
        """
        print("Bienvenue au Blackjack !")

        # Distribution initiale
        self.main_joueur = [self.sabot.tirer_carte(), self.sabot.tirer_carte()]
        self.main_croupier = [self.sabot.tirer_carte(), self.sabot.tirer_carte()]

        # Affiche les cartes initiales
        self.afficher_main("Joueur", self.main_joueur)
        print("\nCarte visible du croupier:")
        print(f"  - {self.main_croupier[0]}")

        # Tour du joueur
        while True:
            valeur_joueur = self.calculer_valeur_main(self.main_joueur)

            if valeur_joueur > 21:
                print("\nVous avez dépassé 21 ! Vous perdez.")
                return

            action = input("\nVoulez-vous tirer une carte (tapez 't') ou rester (tapez 'r') ? ")

            if action == "t":
                self.main_joueur.append(self.sabot.tirer_carte())
                self.afficher_main("Joueur", self.main_joueur)
            elif action == "r":
                break
            else:
                print("Action invalide. Veuillez taper 't' pour tirer ou 'r' pour rester.")

        # Tour du croupier
        print("\nTour du croupier :")
        self.afficher_main("Croupier", self.main_croupier)

        while self.calculer_valeur_main(self.main_croupier) < 17:
            carte = self.sabot.tirer_carte()
            self.main_croupier.append(carte)
            print(f"\nLe croupier tire une carte : {carte}")
            self.afficher_main("Croupier", self.main_croupier)

        # Résultats finaux
        valeur_joueur = self.calculer_valeur_main(self.main_joueur)
        valeur_croupier = self.calculer_valeur_main(self.main_croupier)

        print("\nRésultats finaux :")
        self.afficher_main("Joueur", self.main_joueur)
        self.afficher_main("Croupier", self.main_croupier)

        if valeur_croupier > 21 or valeur_joueur > valeur_croupier:
            print("\nFélicitations, vous gagnez !")
        elif valeur_joueur < valeur_croupier:
            print("\nLe croupier gagne. Vous perdez.")
        else:
            print("\nÉgalité !")


# Exemple d'utilisation autonome
if __name__ == "__main__":
    while True:
        jeu = BlackJack()
        jeu.jouer()

        rejouer = input("\nVoulez-vous rejouer ? (O pour oui, Q pour quitter) : ").lower()
        if rejouer == "q":
            print("Merci d'avoir joué ! À bientôt.")
            break
