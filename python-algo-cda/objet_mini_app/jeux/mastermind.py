"""Règles de base

    Combinaison secrète : L'ordinateur choisit une combinaison de 4 chiffres entre 1 et 6.
    Objectif : Le joueur doit deviner cette combinaison en un nombre limité d'essais (par exemple, 10 essais).
    Indications : À chaque essai, l'ordinateur donne des indications :
        Un pion noir indique qu'un chiffre est correct et bien placé.
        Un pion blanc indique qu'un chiffre est correct mais mal placé."""

import random

def generer_combinaison():
    """Génère une combinaison secrète de 4 chiffres entre 1 et 6"""
    return [random.randint(1, 6) for _ in range(4)]

def evaluer_proposition(proposition, combinaison_secrete):
    """Évalue la proposition du joueur en fonction de la combinaison secrète
        et retourne les pions noirs et blancs."""
    noirs = 0  # Compte des chiffres corrects et bien placés
    blancs = 0  # Compte des chiffres corrects mais mal placés
    
    # Création de copies pour éviter de modifier les listes d'origine
    combinaison_secrete_copy = combinaison_secrete[:]
    proposition_copy = proposition[:]
    
    # Vérification des pions noirs (chiffres corrects et bien placés)
    for i in range(4):
        if proposition[i] == combinaison_secrete_copy[i]:
            noirs += 1
            # Marque les chiffres trouvés pour éviter de les compter à nouveau
            combinaison_secrete_copy[i] = proposition_copy[i] = None

    # Vérification des pions blancs (chiffres corrects mais mal placés)
    for i in range(4):
        if proposition_copy[i] is not None and proposition_copy[i] in combinaison_secrete_copy:
            blancs += 1
            # Marque le chiffre comme utilisé pour éviter de le recompter
            combinaison_secrete_copy[combinaison_secrete_copy.index(proposition_copy[i])] = None

    return noirs, blancs

def mastermind():
    # Génère la combinaison secrète de 4 chiffres entre 1 et 6 que le joueur doit deviner
    combinaison_secrete = generer_combinaison()
    essais_max = 10  # Nombre maximal d'essais pour deviner la combinaison
    print("Bienvenue au Mastermind ! Devinez la combinaison de 4 chiffres entre 1 et 6.")
    print("Un pion noir signifie qu'un chiffre est correct et bien placé.")
    print("Un pion blanc signifie qu'un chiffre est correct mais mal placé.")
    
    # Boucle principale de jeu pour les 10 essais
    for essai in range(essais_max):
        # Demande au joueur de saisir une combinaison de 4 chiffres
        proposition = input(f"\nEssai {essai + 1}/{essais_max} : Entrez votre combinaison de 4 chiffres : ")
        
        # Convertit l'entrée en une liste d'entiers
        proposition = list(map(int, proposition.split()))
        
        # Vérifie que l'entrée est valide (4 chiffres entre 1 et 6)
        if len(proposition) != 4 or any(chiffre < 1 or chiffre > 6 for chiffre in proposition):
            print("Entrée invalide ! Assurez-vous d'entrer 4 chiffres entre 1 et 6.")
            continue  # Redemande une nouvelle entrée en cas d'erreur
        
        # Évalue la proposition du joueur par rapport à la combinaison secrète
        noirs, blancs = evaluer_proposition(proposition, combinaison_secrete)
        print(f"Résultat : {noirs} pion(s) noir(s), {blancs} pion(s) blanc(s)")
        
        # Vérifie si le joueur a trouvé la combinaison (4 pions noirs)
        if noirs == 4:
            print("Félicitations ! Vous avez deviné la combinaison secrète.")
            return  # Fin du jeu en cas de victoire
    
    # Si le joueur n'a pas trouvé après tous les essais, révèle la combinaison
    print(f"Dommage ! Vous avez épuisé vos essais. La combinaison secrète était : {combinaison_secrete}")

# Démarre le jeu
if __name__ == "__main__":
    mastermind()
