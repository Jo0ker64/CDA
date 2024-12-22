"""
Regles du jeu

Le Uno est un jeu de cartes où le but est d'être le premier à se débarrasser de toutes ses cartes. Voici les règles principales du Uno :

### Objectif
Le but du jeu est d'être le premier joueur à se débarrasser de toutes ses cartes. Les joueurs gagnent des points pour les cartes qui restent dans la main de leurs adversaires.

### Configuration
- Chaque joueur commence avec **7 cartes**. Les cartes restantes forment une pioche au centre.
- Une carte est tirée de la pioche et placée face visible pour démarrer la pile de défausse.

### Types de Cartes
Le jeu Uno comporte **108 cartes** de différentes couleurs et types :

#### 1. **Cartes Numériques**
   - Il y a des cartes numérotées de **0 à 9** dans chaque couleur (Rouge, Jaune, Vert, Bleu).
   - Chaque couleur possède deux exemplaires de chaque carte numérique, sauf pour le **0**, qui n’a qu'un seul exemplaire.

#### 2. **Cartes d’Action**
   - **Passer le tour** (1 par couleur) : Le joueur suivant doit passer son tour.
   - **Inverser le sens** (1 par couleur) : Change la direction du jeu. En jeu à deux joueurs, cela revient à passer le tour de l’adversaire.
   - **+2** (1 par couleur) : Le joueur suivant pioche deux cartes et passe son tour.

#### 3. **Cartes Spéciales Noires**
   - **+4** (4 cartes) : Le joueur suivant doit piocher 4 cartes et passer son tour. Le joueur qui joue cette carte choisit la couleur de la prochaine carte.
   - **Changement de couleur** (4 cartes) : Le joueur choisit la couleur de la prochaine carte.

### Déroulement d’un Tour
1. **Jouer une Carte** : Les joueurs doivent jouer une carte de leur main qui correspond à la couleur ou au type de la carte sur la pile de défausse.
2. **Carte Injouable** : Si un joueur ne peut pas jouer, il doit piocher une carte. S’il peut jouer cette carte, il peut la jouer immédiatement, sinon il passe son tour.
3. **Cartes d’Action et Spéciales** : Lorsqu’un joueur joue une carte d’action ou une carte spéciale, son effet s'applique immédiatement.

### Règles des Cartes Spéciales
- **Passer le tour** : Le joueur suivant passe son tour.
- **Inverser le sens** : La direction du jeu est inversée.
- **+2** : Le joueur suivant doit piocher deux cartes et passe son tour.
- **Changement de couleur** : Le joueur peut changer la couleur de la pile de défausse.
- **+4** : Le joueur suivant doit piocher quatre cartes et passe son tour. La couleur de la pile de défausse est également changée. Cette carte ne peut être jouée que si le joueur ne peut pas jouer une carte de la couleur demandée.

### Règle du « Uno »
Lorsque le joueur n’a plus qu’une carte en main, il doit dire « Uno ». S’il oublie et qu’un autre joueur le signale avant son tour suivant, il doit piocher deux cartes en pénalité.

### Fin de la Partie
La manche se termine lorsqu'un joueur n’a plus de cartes. Les autres joueurs comptent les points des cartes restantes dans leurs mains, qui sont ajoutés au score du gagnant :

- Cartes numériques : Valeur du chiffre.
- Cartes d’Action (+2, Passer le tour, Inverser) : 20 points.
- Cartes Spéciales (+4 et Changement de couleur) : 50 points.

### Fin du Jeu
Le jeu continue sur plusieurs manches jusqu’à ce qu'un joueur atteigne **500 points** (ou un autre score déterminé au début de la partie). Le joueur avec le score le plus élevé gagne le jeu.

"""
import random
from collections import Counter


class Carte:
    """
    Classe représentant une carte Uno.
    """
    def __init__(self, couleur, type):
        self.couleur = couleur
        self.type = type

    def peut_recouvrir(self, autre_carte):
        """
        Vérifie si cette carte peut être jouée sur une autre carte.
        """
        return (self.couleur == autre_carte.couleur or
                self.type == autre_carte.type or
                self.couleur == "Noir")

    def __str__(self):
        """
        Représentation en chaîne pour affichage.
        """
        return f"{self.couleur} {self.type}"


class JeuUno:
    """
    Classe pour créer et gérer le jeu de cartes Uno.
    """
    def __init__(self):
        self.cartes = self.creer_jeu()
        random.shuffle(self.cartes)

    def creer_jeu(self):
        """
        Crée un jeu de Uno complet avec toutes les cartes.
        """
        couleurs = ["Rouge", "Jaune", "Vert", "Bleu"]
        types_numeriques = list(range(10)) + list(range(1, 10))
        cartes_speciales = ["⦸", "⟲", "+2"]
        cartes_noires = ["+4", "Changement de couleur"]
        jeu = []

        for couleur in couleurs:
            for type in types_numeriques:
                jeu.append(Carte(couleur, type))
            for carte_speciale in cartes_speciales:
                jeu.append(Carte(couleur, carte_speciale))

        for carte_noire in cartes_noires:
            for _ in range(4):
                jeu.append(Carte("Noir", carte_noire))

        return jeu

    def piocher(self, nombre=1):
        """
        Pioche une ou plusieurs cartes depuis le jeu.
        """
        return [self.cartes.pop() for _ in range(nombre)]


class Joueur:
    """
    Classe représentant un joueur Uno.
    """
    def __init__(self, nom, type_joueur="humain"):
        self.nom = nom
        self.type_joueur = type_joueur
        self.main = []

    def ajouter_cartes(self, cartes):
        """
        Ajoute une ou plusieurs cartes à la main du joueur.
        """
        self.main.extend(cartes)

    def jouer_carte(self, derniere_carte):
        """
        Permet au joueur de jouer une carte ou de piocher s'il ne peut pas jouer.
        """
        if self.type_joueur == "humain":
            return self.jouer_carte_humain(derniere_carte)
        else:
            return self.jouer_carte_ordinateur(derniere_carte)

    def jouer_carte_humain(self, derniere_carte):
        """
        Permet au joueur humain de choisir une carte.
        """
        while True:
            self.afficher_main()
            choix = input("Choisissez une carte à jouer (numéro) ou tapez 0 pour piocher : ")
            try:
                choix = int(choix) - 1
                if choix == -1:
                    return None
                carte = self.main[choix]
                if carte.peut_recouvrir(derniere_carte):
                    return self.main.pop(choix)
                else:
                    print("Cette carte ne peut pas être jouée.")
            except (IndexError, ValueError):
                print("Entrée invalide. Veuillez réessayer.")

    def jouer_carte_ordinateur(self, derniere_carte):
        """
        L'ordinateur joue la première carte jouable ou pioche.
        """
        for carte in self.main:
            if carte.peut_recouvrir(derniere_carte):
                self.main.remove(carte)
                print(f"L'ordinateur joue : {carte}")
                return carte
        return None

    def choisir_couleur(self):
        """
        Choisit une couleur pour une carte noire.
        """
        couleurs = [carte.couleur for carte in self.main if carte.couleur in ["Rouge", "Jaune", "Vert", "Bleu"]]
        if self.type_joueur == "humain":
            return input("Choisissez une couleur (Rouge, Jaune, Vert, Bleu) : ")
        else:
            couleur_freq = Counter(couleurs).most_common(1)[0][0] if couleurs else random.choice(["Rouge", "Jaune", "Vert", "Bleu"])
            print(f"L'ordinateur choisit : {couleur_freq}")
            return couleur_freq

    def afficher_main(self):
        """
        Affiche les cartes dans la main du joueur.
        """
        print(f"\nMain de {self.nom}:")
        for index, carte in enumerate(self.main, start=1):
            print(f"{index}. {carte}")

    def __str__(self):
        return self.nom


class PartieUno:
    """
    Classe principale pour gérer une partie de Uno.
    """
    def __init__(self):
        self.jeu = JeuUno()
        self.joueurs = self.initialiser_joueurs()
        self.derniere_carte = self.jeu.piocher()[0]
        self.sens = 1  # 1 pour horaire, -1 pour antihoraire
        self.joueur_actuel_index = 0

    def initialiser_joueurs(self):
        """
        Initialise les joueurs avec leur type (humain ou ordinateur).
        """
        joueurs = []
        nombre_joueurs = int(input("Combien de joueurs ? "))
        for i in range(nombre_joueurs):
            nom = input(f"Nom du joueur {i + 1} : ")
            type_joueur = input("Type (humain/ordinateur) : ").strip().lower()
            joueurs.append(Joueur(nom, type_joueur))
        self.distribuer_cartes(joueurs)
        return joueurs

    def distribuer_cartes(self, joueurs):
        """
        Distribue 7 cartes à chaque joueur.
        """
        for joueur in joueurs:
            joueur.ajouter_cartes(self.jeu.piocher(7))

    def afficher_carte_a_recouvrir(self):
        """
        Affiche la dernière carte jouée.
        """
        print(f"\nCarte à recouvrir : {self.derniere_carte}")

    def jouer_tour(self):
        """
        Joue un tour pour le joueur actuel.
        """
        joueur = self.joueurs[self.joueur_actuel_index]
        print(f"\nTour de {joueur.nom}")
        self.afficher_carte_a_recouvrir()

        carte_jouee = joueur.jouer_carte(self.derniere_carte)

        if carte_jouee:
            self.derniere_carte = carte_jouee
            if carte_jouee.type in ["+4", "Changement de couleur"]:
                self.derniere_carte.couleur = joueur.choisir_couleur()
            elif carte_jouee.type == "+2":
                prochain_joueur = self.joueurs[(self.joueur_actuel_index + self.sens) % len(self.joueurs)]
                prochain_joueur.ajouter_cartes(self.jeu.piocher(2))
            elif carte_jouee.type == "⟲":
                self.sens *= -1
            elif carte_jouee.type == "⦸":
                self.joueur_actuel_index = (self.joueur_actuel_index + self.sens) % len(self.joueurs)
        else:
            joueur.ajouter_cartes(self.jeu.piocher())

        if not joueur.main:
            print(f"{joueur.nom} a gagné !")
            return True

        self.joueur_actuel_index = (self.joueur_actuel_index + self.sens) % len(self.joueurs)
        return False

    def lancer_partie(self):
        """
        Lance la partie de Uno.
        """
        while True:
            if self.jouer_tour():
                break


# Exemple d'exécution
if __name__ == "__main__":
    partie = PartieUno()
    partie.lancer_partie()
