import random

# Dictionnaire de symboles Unicode pour chaque carte
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

# Créer le sabot de cartes avec 4 jeux de 52 cartes en utilisant des dictionnaires
def creer_sabot():
    """Retourne un sabot de 4 jeux de 52 cartes sous forme de dictionnaires"""
    sabot = []
    valeurs = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "V": 10, "D": 10, "R": 10, "A": 11
    }
    couleurs = ["♥", "♦", "♠", "♣"]
    
    # Ajouter 4 jeux de cartes au sabot
    for _ in range(4):
        for couleur in couleurs:
            for valeur, points in valeurs.items():
                sabot.append({"valeur": valeur, "couleur": couleur, "points": points})
    
    random.shuffle(sabot)
    return sabot

# Calculer la valeur d'une main
def calculer_valeur_main(main):
    """Calcule la valeur d'une main"""
    valeur_totale = 0
    nombre_as = 0
    for carte in main:
        valeur_totale += carte["points"]
        if carte["valeur"] == "A":
            nombre_as += 1
    
    # Ajuster pour les As
    while valeur_totale > 21 and nombre_as:
        valeur_totale -= 10
        nombre_as -= 1
    
    return valeur_totale

# Afficher la main de manière lisible
def afficher_main(joueur, main):
    """Affiche la main d'un joueur avec chaque carte en utilisant les symboles Unicode"""
    print(f"\nMain de {joueur} :")
    for carte in main:
        symbole = cartes_unicode[(carte['valeur'], carte['couleur'])]
        print(f"  - {symbole}")
    print(f"Valeur totale: {calculer_valeur_main(main)}")

# Fonction principale de jeu
def jouer_blackjack():
    sabot = creer_sabot()
    
    # Distribuer les cartes initiales
    main_joueur = [sabot.pop(), sabot.pop()]
    main_croupier = [sabot.pop(), sabot.pop()]
    
    # Afficher les cartes initiales
    afficher_main("Joueur", main_joueur)
    print("\nCarte visible du croupier:")
    print(f"  - {cartes_unicode[(main_croupier[0]['valeur'], main_croupier[0]['couleur'])]}")
    
    # Tour du joueur
    while True:
        valeur_joueur = calculer_valeur_main(main_joueur)
        
        if valeur_joueur > 21:
            print("\nVous avez dépassé 21 ! Vous perdez.")
            return
        
        action = input("\nVoulez-vous tirer une carte (tapez 't') ou rester (tapez 'r') ? ")
        
        if action == "t":
            main_joueur.append(sabot.pop())
            afficher_main("Joueur", main_joueur)
        elif action == "r":
            break
        else:
            print("Action invalide. Veuillez taper 't' pour tirer ou 'r' pour rester.")

    # Tour du croupier
    print("\nTour du croupier :")
    afficher_main("Croupier", main_croupier)
    
    while calculer_valeur_main(main_croupier) < 17:
        main_croupier.append(sabot.pop())
        print(f"\nLe croupier tire une carte : {cartes_unicode[(main_croupier[-1]['valeur'], main_croupier[-1]['couleur'])]}")
        afficher_main("Croupier", main_croupier)

    # Résultats finaux
    valeur_joueur = calculer_valeur_main(main_joueur)
    valeur_croupier = calculer_valeur_main(main_croupier)
    
    print("\nRésultats finaux :")
    afficher_main("Joueur", main_joueur)
    afficher_main("Croupier", main_croupier)
    
    if valeur_croupier > 21 or valeur_joueur > valeur_croupier:
        print("\nFélicitations, vous gagnez !")
    elif valeur_joueur < valeur_croupier:
        print("\nLe croupier gagne. Vous perdez.")
    else:
        print("\nÉgalité !")

# Démarrer le jeu
if __name__ == "__main__":
    jouer_blackjack()

while True:
        jouer_blackjack()
    
        # Demander si le joueur veut rejouer ou quitter
        while True:
            rejouer = input("\nVoulez-vous jouer une autre partie ? (tapez 'O' pour oui ou 'Q' pour quitter) : ")
            if rejouer.lower() == 'q':
                print("Merci d'avoir joué ! À bientôt.")
                exit()  # Quitter le programme
            elif rejouer.lower() == 'o':
                break  # Sortir de la boucle de demande et recommencer une partie
            else:
                print("Action invalide. Veuillez taper 'O' pour oui ou 'Q' pour quitter")
