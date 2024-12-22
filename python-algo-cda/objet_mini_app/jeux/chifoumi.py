
import random

def chifoumi():
    # Définition des règles du jeu avec les messages spécifiques
    regles = {
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

    for choix, resultats in regles.items():
        for adversaire, message in resultats.items():
            print(message)

    choix = list(regles.keys())

    while True:
        Sheldon = input("Choisissez Pierre, Feuille, Ciseaux, Lézard, Spock (ou 'Q' pour quitter) : ") #.capitalize() permet de mettre la premiere lettre des mots en majuscule et le reste en minuscule
        
        if Sheldon == 'Q':
            break
        
        if Sheldon not in choix:
            print("Choix invalide, veuillez réessayer.")
            continue
        
        Howard = random.choice(choix)
        print(f"Howard a choisi : {Howard}")

        if Sheldon == Howard:
            print("Égalité !")
        elif Howard in regles[Sheldon]:
            print("Sheldon gagne !")
            print(regles[Sheldon][Howard])
        else:
            print("Sheldon perds !")
            print(regles[Howard][Sheldon])
    
    print("Merci d'avoir joué !")

# Lancer le jeu
if __name__ == "__main__":
    chifoumi()
