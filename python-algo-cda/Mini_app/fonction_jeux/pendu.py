print("Lancement du Jeu du pendu ...")

import random

def choisir_mot():
    mots = ["python", "ordinateur", "programmation", "intelligence", "algorithme"]
    return random.choice(mots).upper()

def afficher_mot(mot, lettres_trouvees):
    affichage = [lettre if lettre in lettres_trouvees else "_" for lettre in mot]
    return " ".join(affichage)

def afficher_pendu(tentatives):
    if tentatives >= 6:
        print(" ==========Y= ")
    if tentatives >= 5:
        print(" ||/       |  ")
    if tentatives >= 4:
        print(" ||        0  ")
    if tentatives >= 3:
        print(" ||       /|\ ")
    if tentatives >= 2:
        print(" ||       / \ ")
    if tentatives >= 1:                    
        print("/||           ")
    if tentatives >= 0:
        print("==============\n")

def pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()
    tentatives = 0
    lettres_essayees = set()

    while tentatives < 6:
        print("\nMot à deviner :", afficher_mot(mot_a_deviner, lettres_trouvees))
        afficher_pendu(tentatives)
        print("Lettres essayées :", " ".join(sorted(lettres_essayees)))
        print("Essais restants :", 6 - tentatives)

        lettre = input("Proposez une lettre : ").upper()

        if lettre in lettres_essayees:
            print("Vous avez déjà essayé cette lettre.")
            continue

        lettres_essayees.add(lettre)

        if lettre in mot_a_deviner:
            lettres_trouvees.add(lettre)
            print("Bonne lettre !")
        else:
            tentatives += 1
            print("Mauvaise lettre.")

        if all(l in lettres_trouvees for l in mot_a_deviner):
            print("\nFélicitations ! Vous avez deviné le mot :", mot_a_deviner)
            break
    else:
        print("\nVous avez perdu ! Le mot était :", mot_a_deviner)
        afficher_pendu(6)  # Affiche le pendu complet à la fin si le joueur perd

if __name__ == "__main__":
    pendu()
