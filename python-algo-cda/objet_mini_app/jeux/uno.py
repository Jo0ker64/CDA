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
# Importation des modules nécessaires
import random
from collections import Counter

# Fonction pour créer le jeu de cartes Uno
def creer_jeu_uno():
    """Crée un jeu de Uno avec des cartes de différentes couleurs et types"""
    # Définition des couleurs et types de cartes
    couleurs = ["Rouge", "Jaune", "Vert", "Bleu"]
    types_numeriques = list(range(10)) + list(range(1, 10))  # 0 à 9, puis 1 à 9
    cartes_speciales = ["⦸", "⟲", "+2"]
    cartes_noires = ["+4", "Changement de couleur"]
    
    jeu = []
    
    # Création des cartes numériques et spéciales pour chaque couleur
    for couleur in couleurs:
        for type in types_numeriques:
            jeu.append({"couleur": couleur, "type": type})
        for carte_speciale in cartes_speciales:
            jeu.append({"couleur": couleur, "type": carte_speciale})
    
    # Ajout des cartes noires (sans couleur spécifique)
    for carte_noire in cartes_noires:
        for _ in range(4):
            jeu.append({"couleur": "Noir", "type": carte_noire})
    
    # Mélange du jeu
    random.shuffle(jeu)
    return jeu

# Fonction pour distribuer les cartes aux joueurs
def distribuer_cartes(jeu, joueurs):
    """Distribue 7 cartes à chaque joueur depuis le jeu"""
    for joueur in joueurs:
        joueur['main'] = [jeu.pop() for _ in range(7)]

# Fonction pour vérifier si une carte peut être jouée
def peut_jouer(carte, derniere_carte):
    """Vérifie si la carte peut être jouée en fonction de la dernière carte jouée"""
    return (carte["couleur"] == derniere_carte["couleur"] or 
            carte["type"] == derniere_carte["type"] or 
            carte["couleur"] == "Noir")

# Fonction pour afficher la main d'un joueur
def afficher_main(joueur):
    """Affiche la main d'un joueur avec chaque carte sur une ligne distincte"""
    print(f"\nMain de {joueur['nom']} ({'Ordinateur' if joueur['type'] == 'ordinateur' else 'Humain'}):")
    for index, carte in enumerate(joueur['main'], start=1):
        print(f" {index}. {carte['couleur']} {carte['type']}")

# Fonction pour afficher la carte à recouvrir
def afficher_carte_a_recouvrir(derniere_carte):
    """Affiche la carte que le joueur doit recouvrir"""
    print("\nCarte à recouvrir :")
    print(f" >>> {derniere_carte['couleur']} {derniere_carte['type']} <<<")

# Fonction pour permettre au joueur humain de choisir une carte
def choisir_carte_humain(joueur, derniere_carte):
    """Permet au joueur humain de choisir une carte jouable"""
    while True:
        try:
            choix = int(input("Choisissez une carte à jouer (numéro) ou tapez 0 pour piocher : ")) - 1
            if choix == -1:
                return None  # Signifie que le joueur veut piocher
            carte = joueur['main'][choix]
            if peut_jouer(carte, derniere_carte):
                return carte
            else:
                print("Cette carte ne peut pas être jouée. Choisissez une autre carte.")
        except (IndexError, ValueError):
            print("Choix invalide. Veuillez entrer un numéro de carte valide.")

# Fonction pour que l'ordinateur choisisse une carte
def choisir_carte_ordinateur(joueur, derniere_carte):
    """L'ordinateur joue la première carte jouable dans sa main"""
    for carte in joueur['main']:
        if peut_jouer(carte, derniere_carte):
            return carte
    return None  # Si aucune carte jouable, il doit piocher

# Fonction pour que l'ordinateur choisisse une couleur
def choisir_couleur_ordinateur(joueur):
    """Choisit la couleur la plus fréquente dans la main de l'ordinateur"""
    couleurs = [carte["couleur"] for carte in joueur["main"] if carte["couleur"] in ["Rouge", "Jaune", "Vert", "Bleu"]]
    if couleurs:
        couleur_freq = Counter(couleurs).most_common(1)[0][0]  # Couleur la plus fréquente
        print(f"L'ordinateur choisit la couleur {couleur_freq}")
        return couleur_freq
    else:
        return random.choice(["Rouge", "Jaune", "Vert", "Bleu"])

# Fonction pour initialiser les joueurs
def initialiser_joueurs():
    """Initialise les joueurs en demandant leur nom et leur type"""
    joueurs = []
    nombre_joueurs = int(input("Combien de joueurs y a-t-il ? "))
    for i in range(nombre_joueurs):
        nom = input(f"Entrez le nom du joueur {i + 1}: ")
        type_joueur = input("Ce joueur est-il un humain ou un ordinateur ? (humain/ordinateur): ").strip().lower()
        joueurs.append({"nom": nom, "type": type_joueur})
    return joueurs

# Fonction principale du jeu
def uno():
    # Initialisation du jeu
    jeu = creer_jeu_uno()
    joueurs = initialiser_joueurs()
    distribuer_cartes(jeu, joueurs)
    derniere_carte = jeu.pop()
    afficher_carte_a_recouvrir(derniere_carte)
    
    joueur_actuel_index = 0
    sens = 1  # 1 pour sens horaire, -1 pour sens antihoraire
    
    # Boucle principale du jeu
    while True:
        joueur_actuel = joueurs[joueur_actuel_index]
        print(f"\nTour de {joueur_actuel['nom']} ({'Ordinateur' if joueur_actuel['type'] == 'ordinateur' else 'Humain'})")
        afficher_main(joueur_actuel)
        afficher_carte_a_recouvrir(derniere_carte)
        
        # Choix de la carte à jouer
        if joueur_actuel["type"] == "humain":
            carte_jouee = choisir_carte_humain(joueur_actuel, derniere_carte)
        else:
            carte_jouee = choisir_carte_ordinateur(joueur_actuel, derniere_carte)
        
        # Jouer la carte ou piocher
        if carte_jouee:
            joueur_actuel['main'].remove(carte_jouee)
            derniere_carte = carte_jouee
            print(f"{joueur_actuel['nom']} joue : {carte_jouee['couleur']} {carte_jouee['type']}")
        else:
            print(f"{joueur_actuel['nom']} doit piocher une carte")
            joueur_actuel['main'].append(jeu.pop())
        
        # Appliquer les effets des cartes spéciales
        if carte_jouee:
            if carte_jouee["type"] == "Passe":
                joueur_actuel_index = (joueur_actuel_index + sens) % len(joueurs)
            elif carte_jouee["type"] == "Inverse":
                sens *= -1
            elif carte_jouee["type"] == "+2":
                prochain_joueur_index = (joueur_actuel_index + sens) % len(joueurs)
                joueurs[prochain_joueur_index]['main'].extend([jeu.pop(), jeu.pop()])
            elif carte_jouee["type"] in ["+4", "Changement de couleur"]:
                if joueur_actuel["type"] == "humain":
                    nouvelle_couleur = input("Choisissez une couleur (Rouge, Jaune, Vert, Bleu) : ")
                else:
                    nouvelle_couleur = choisir_couleur_ordinateur(joueur_actuel)
                derniere_carte["couleur"] = nouvelle_couleur
                if carte_jouee["type"] == "+4":
                    prochain_joueur_index = (joueur_actuel_index + sens) % len(joueurs)
                    joueurs[prochain_joueur_index]['main'].extend([jeu.pop() for _ in range(4)])
        
        # Vérifier si le joueur a gagné
        if not joueur_actuel['main']:
            print(f"{joueur_actuel['nom']} a gagné !")
            break
        
        # Passer au joueur suivant
        joueur_actuel_index = (joueur_actuel_index + sens) % len(joueurs)

# Démarrer le jeu si le script est exécuté directement
if __name__ == "__main__":
    uno()
