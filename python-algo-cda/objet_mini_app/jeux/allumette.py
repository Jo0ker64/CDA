import random

def allumette():
    # Nombre initial d'allumettes
    total_allumettes = 20  

    # Affiche les règles du jeu
    print("Bienvenue au Jeu des Allumettes !")
    print("Règles du jeu :")
    print("- Il y a 20 allumettes sur la table.")
    print("- Vous et l'ordinateur jouez chacun votre tour.")
    print("- À chaque tour, vous pouvez retirer 1, 2 ou 3 allumettes.")
    print("- Le joueur qui est obligé de prendre la dernière allumette perd la partie.")
    print("Essayez d'éviter de prendre la dernière allumette pour gagner !\n")

    # Boucle principale du jeu
    while total_allumettes > 0:
        # Affiche le nombre d'allumettes restantes
        print(f"\nAllumettes restantes : {total_allumettes}")

        # Demande au joueur combien d'allumettes il souhaite retirer
        while True:
            try:
                joueur_retrait = int(input("Combien d'allumettes voulez-vous retirer ? (1, 2 ou 3) : "))
                # Vérifie si le nombre d'allumettes retiré est valide
                if joueur_retrait in [1, 2, 3] and joueur_retrait <= total_allumettes:
                    break  # Sort de la boucle si l'entrée est valide
                else:
                    print("Choix invalide. Essayez à nouveau.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")  # Gestion des erreurs de saisie

        # Met à jour le nombre total d'allumettes après le retrait du joueur
        total_allumettes -= joueur_retrait

        # Vérifie si le joueur a pris la dernière allumette
        if total_allumettes == 0:
            print("Vous avez pris la dernière allumette. Vous avez perdu !")
            break  # Fin du jeu si le joueur a perdu

        # Tour de l'ordinateur : choisit un nombre d'allumettes aléatoire à retirer
        ordi_retrait = random.randint(1, min(3, total_allumettes))
        print(f"L'ordinateur retire {ordi_retrait} allumette(s).")
        
        # Met à jour le nombre total d'allumettes après le retrait de l'ordinateur
        total_allumettes -= ordi_retrait

        # Vérifie si l'ordinateur a pris la dernière allumette
        if total_allumettes == 0:
            print("L'ordinateur a pris la dernière allumette. Vous avez gagné !")
            break  # Fin du jeu si le joueur a gagné

# Point d'entrée du programme
if __name__ == "__main__":
    allumette()  # Lancement du jeu des allumettes
