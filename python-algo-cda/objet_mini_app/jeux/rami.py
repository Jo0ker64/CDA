import random

# Dictionnaire des cartes avec leurs représentations Unicode
cartes = {
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

    (15, "J"): "Joker", 
}

def creer_jeu():
    jeu = list(cartes.keys())
    random.shuffle(jeu)
    return jeu

def trier_main_par_couleur_et_valeur(main):
    main.sort(key=lambda carte: (carte[1], carte[0]))

def trier_main_par_valeur(main):
    main.sort(key=lambda carte: (carte[0], carte[1]))

def distribuer_cartes(jeu):
    mains = {"joueur": jeu[:15], "ordi": jeu[15:29]}
    pioche = jeu[29:]
    defausse = [pioche.pop()]
    trier_main_par_couleur_et_valeur(mains["joueur"])
    trier_main_par_couleur_et_valeur(mains["ordi"])
    return mains, pioche, defausse

def afficher_carte(carte):
    return cartes[carte]

def afficher_main(mains, joueur="joueur"):
    print("\nVotre main :")
    for i, carte in enumerate(mains[joueur], start=1):
        print(f"{i}: {afficher_carte(carte)}")

def est_suite(cartes):
    valeurs = sorted([carte[0] for carte in cartes])
    couleurs = [carte[1] for carte in cartes]
    
    if len(set(couleurs)) != 1:
        return False

    if valeurs == list(range(valeurs[0], valeurs[0] + len(cartes))):
        return True

    if valeurs[-1] == 1:
        valeurs[-1] = 15
        if valeurs == list(range(valeurs[0], valeurs[0] + len(cartes))):
            return True

    return False

def est_groupe(cartes):
    valeurs = [carte[0] for carte in cartes]
    couleurs = [carte[1] for carte in cartes]
    return len(set(valeurs)) == 1 and len(set(couleurs)) == len(cartes)

def piocher(pioche, defausse):
    if pioche:
        return pioche.pop(0)
    else:
        random.shuffle(defausse)
        return defausse.pop(0)

def tour_joueur(mains, pioche, defausse, premier_tour=False):
    print("\n--- Votre Tour ---")
    print(f"Cartes restantes pour l'ordinateur : {len(mains['ordi'])}")

    choix_tri = input("Voulez-vous trier vos cartes par (1) Couleur et Valeur ou (2) Valeur ? ")
    if choix_tri == "2":
        trier_main_par_valeur(mains["joueur"])
    else:
        trier_main_par_couleur_et_valeur(mains["joueur"])

    afficher_main(mains)
    print(f"Carte au sommet de la défausse : {afficher_carte(defausse[-1])}")

    if premier_tour:
        print("Premier tour : Vous ne pouvez pas piocher. Veuillez défausser une carte.")
    else:
        choix_piocher = input("Voulez-vous piocher de la pioche (P) ou de la défausse (D) ? ").strip().upper()
        if choix_piocher == 'D':
            carte_piochee = defausse.pop()
        else:
            carte_piochee = piocher(pioche, defausse)
        mains["joueur"].append(carte_piochee)
        print(f"Vous avez pioché : {afficher_carte(carte_piochee)}")

        if choix_tri == "2":
            trier_main_par_valeur(mains["joueur"])
        else:
            trier_main_par_couleur_et_valeur(mains["joueur"])

        afficher_main(mains)

    while True:
        try:
            indices = input("Entrez les indices des cartes pour une combinaison valide (ex: 1 2 3), ou appuyez sur Entrée pour passer : ")
            if not indices:
                break
            indices = list(map(int, indices.split()))
            combinaison = [mains["joueur"][i - 1] for i in indices]

            if len(combinaison) >= 3 and (est_suite(combinaison) or est_groupe(combinaison)):
                print("Combinaison valide :", " ".join(afficher_carte(c) for c in combinaison))
                for carte in combinaison:
                    mains["joueur"].remove(carte)
                break
            else:
                print("Combinaison non valide.")
        except (ValueError, IndexError):
            print("Entrée non valide. Essayez à nouveau.")

    afficher_main(mains)
    choix_defausse = int(input("Choisissez la carte à défausser : ")) - 1
    defausse.append(mains["joueur"].pop(choix_defausse))
    print(f"Vous avez défaussé : {afficher_carte(defausse[-1])}")

    if choix_tri == "2":
        trier_main_par_valeur(mains["joueur"])
    else:
        trier_main_par_couleur_et_valeur(mains["joueur"])

def tour_ordi(mains, pioche, defausse):
    print("\n--- Tour de l'ordinateur ---")
    carte_piochee = piocher(pioche, defausse)
    mains["ordi"].append(carte_piochee)

    trier_main_par_couleur_et_valeur(mains["ordi"])

    combinaison_trouvee = False
    for i in range(len(mains["ordi"])):
        for j in range(i + 1, len(mains["ordi"])):
            for k in range(j + 1, len(mains["ordi"])):
                combinaison = [mains["ordi"][i], mains["ordi"][j], mains["ordi"][k]]
                if est_suite(combinaison) or est_groupe(combinaison):
                    print("L'ordinateur pose une combinaison :", " ".join(afficher_carte(c) for c in combinaison))
                    for carte in combinaison:
                        mains["ordi"].remove(carte)
                    combinaison_trouvee = True
                    break
            if combinaison_trouvee:
                break
        if combinaison_trouvee:
            break

    defausse.append(mains["ordi"].pop(random.randint(0, len(mains["ordi"]) - 1)))
    print(f"L'ordinateur a défaussé une carte.\n")

def jeu_rami():
    jeu = creer_jeu()
    mains, pioche, defausse = distribuer_cartes(jeu)

    print("Bienvenue au jeu de Rami !")

    tour_joueur(mains, pioche, defausse, premier_tour=True)

    while mains["joueur"] and mains["ordi"]:
        tour_ordi(mains, pioche, defausse)
        if not mains["ordi"]:
            print("L'ordinateur a gagné la partie.")
            return

        tour_joueur(mains, pioche, defausse)
        if not mains["joueur"]:
            print("Félicitations ! Vous avez gagné la partie.")
            return

    print("Partie terminée.")

if __name__ == "__main__":
    jeu_rami()
