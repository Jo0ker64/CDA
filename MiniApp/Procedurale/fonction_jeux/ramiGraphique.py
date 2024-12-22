import random
import pygame
import os
import pygame_gui

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 128, 0)
ROUGE = (255, 0, 0)

# Définition de la taille de la fenêtre
LARGEUR = 1200
HAUTEUR = 768

# Création de la fenêtre de jeu avec les dimensions spécifiées
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de Rami")

# Chemin vers le dossier des images de cartes
chemin_images = r"C:\laragon\www\CDA\python\Mini_app\fonction_jeux\cartes"

# Génère le nom de fichier d'image d'une carte en fonction de sa valeur et de sa couleur
def get_nom_carte(valeur, couleur):
    if couleur == "J1":
        return "JR"  # Joker rouge
    elif couleur == "J2":
        return "JN"  # Joker noir

    symboles = {"♠": "s", "♥": "h", "♦": "d", "♣": "c"}
    noms_speciaux = {1: "A", 11: "J", 12: "Q", 13: "K"}
    return noms_speciaux.get(valeur, str(valeur)) + symboles[couleur]

# Chargement des images des cartes dans un dictionnaire
images_cartes = {}
for valeur in range(1, 15):
    for couleur in ["♠", "♥", "♦", "♣", "J1", "J2"]:
        if valeur == 14 and couleur not in ["J1", "J2"]:
            continue
        nom_carte = get_nom_carte(valeur, couleur)
        chemin_complet = os.path.join(chemin_images, f"{nom_carte}.gif")
        if os.path.exists(chemin_complet):
            images_cartes[(valeur, couleur)] = pygame.image.load(chemin_complet)

# Fonction pour créer un jeu de cartes mélangé
def creer_jeu():
    jeu = [(valeur, couleur) for valeur in range(1, 14) for couleur in ["♠", "♥", "♦", "♣"]] * 2
    jeu += [(14, "J1"), (14, "J2")]
    random.shuffle(jeu)
    return jeu

# Trie la main en fonction de la couleur et de la valeur des cartes
def trier_main_par_couleur_et_valeur(main):
    main.sort(key=lambda carte: (carte[1], carte[0]))

# Distribue les cartes aux joueurs, crée la pioche et la défausse
def distribuer_cartes(jeu):
    mains = {"joueur": jeu[:15], "ordi": jeu[15:29]}
    pioche = jeu[29:]
    defausse = [pioche.pop()]
    trier_main_par_couleur_et_valeur(mains["joueur"])
    trier_main_par_couleur_et_valeur(mains["ordi"])
    return mains, pioche, defausse

# Vérifie si une liste de cartes forme une suite, en utilisant le joker si nécessaire
def est_suite(cartes):
    valeurs = sorted([carte[0] for carte in cartes if carte[0] != 14])
    couleurs = [carte[1] for carte in cartes if carte[0] != 14]
    nombre_jokers = len([carte for carte in cartes if carte[0] == 14])

    # Toutes les cartes doivent être de la même couleur, ou être compensées par des jokers
    if len(set(couleurs)) != 1 and nombre_jokers < len(cartes) - 1:
        return False

    if len(valeurs) + nombre_jokers < 3:
        return False

    # Vérifie la séquence des valeurs avec les jokers
    for i in range(len(valeurs) - 1):
        difference = valeurs[i + 1] - valeurs[i]
        if difference > 1 + nombre_jokers:
            return False
        nombre_jokers -= max(0, difference - 1)

    return True

# Vérifie si une liste de cartes forme un groupe (même valeur), en utilisant le joker si nécessaire
def est_groupe(cartes):
    valeurs = [carte[0] for carte in cartes if carte[0] != 14]
    jokers = [carte for carte in cartes if carte[0] == 14]
    
    if len(set(valeurs)) > 1 and len(jokers) == 0:
        return False
    
    # Si toutes les cartes ont la même valeur ou sont jokers, c'est un groupe valide
    return len(cartes) >= 3 and len(cartes) <= 4

# Tire une carte de la pioche, ou de la défausse si la pioche est vide
def piocher(pioche, defausse):
    if pioche:
        return pioche.pop(0)
    else:
        random.shuffle(defausse)
        return defausse.pop(0)

# Affiche une carte à l'écran aux coordonnées spécifiées
def afficher_carte_graphique(fenetre, carte, x, y):
    if carte in images_cartes:
        fenetre.blit(images_cartes[carte], (x, y))
    else:
        couleur = ROUGE if carte[1] in ["♥", "♦"] else NOIR
        pygame.draw.rect(fenetre, BLANC, (x, y, 71, 96))
        pygame.draw.rect(fenetre, couleur, (x, y, 71, 96), 2)
        font = pygame.font.Font(None, 24)
        texte = font.render(get_nom_carte(*carte), True, couleur)
        fenetre.blit(texte, (x + 5, y + 35))

# Affiche les cartes d'une main (joueur ou ordinateur)
def afficher_main_graphique(fenetre, main, y):
    for i, carte in enumerate(main):
        afficher_carte_graphique(fenetre, carte, i * 80 + 10, y)

# Affiche l'interface du jeu, y compris les mains, la défausse et les combinaisons
def afficher_interface(fenetre, mains, defausse, combinaisons):
    fenetre.fill(VERT)
    afficher_main_graphique(fenetre, mains["joueur"], HAUTEUR - 150)
    afficher_carte_graphique(fenetre, defausse[-1], LARGEUR // 2 - 35, HAUTEUR // 2 - 48)
    
    font = pygame.font.Font(None, 36)
    texte_ordi = font.render(f"Cartes de l'ordinateur : {len(mains['ordi'])}", True, BLANC)
    fenetre.blit(texte_ordi, (10, 10))
    
    texte_defausse = font.render("Défausse", True, BLANC)
    fenetre.blit(texte_defausse, (LARGEUR // 2 - 50, HAUTEUR // 2 - 80))
    
    texte_combinaisons = font.render("Combinaisons :", True, BLANC)
    fenetre.blit(texte_combinaisons, (10, 50))
    for i, combinaison in enumerate(combinaisons):
        for j, carte in enumerate(combinaison):
            afficher_carte_graphique(fenetre, carte, 10 + j * 40, 90 + i * 100)
    
    pygame.display.flip()

# Tour de l'ordinateur, cherchant à former des combinaisons
def tour_ordi(mains, defausse, combinaisons):
    carte_piochee = piocher(mains["ordi"], defausse)
    mains["ordi"].append(carte_piochee)
    trier_main_par_couleur_et_valeur(mains["ordi"])

    # Tentative de combinaison de l'ordinateur
    combinaison_trouvee = False
    for i in range(len(mains["ordi"])):
        for j in range(i + 1, len(mains["ordi"])):
            for k in range(j + 1, len(mains["ordi"])):
                combinaison = [mains["ordi"][i], mains["ordi"][j], mains["ordi"][k]]
                if est_suite(combinaison) or est_groupe(combinaison):
                    combinaisons.append(combinaison)
                    for carte in combinaison:
                        mains["ordi"].remove(carte)
                    combinaison_trouvee = True
                    break
            if combinaison_trouvee:
                break
        if combinaison_trouvee:
            break

    if mains["ordi"]:
        carte_defaussee = mains["ordi"].pop(random.randint(0, len(mains["ordi"]) - 1))
        defausse.append(carte_defaussee)

# Fonction principale du jeu de Rami en mode graphique
def jeu_rami_graphique():
    jeu = creer_jeu()
    mains, pioche, defausse = distribuer_cartes(jeu)
    combinaisons = []

    en_cours = True
    tour_joueur = True
    premier_tour = True
    a_pioche = False
    
    # Création de l'interface utilisateur avec des boutons
    manager = pygame_gui.UIManager((LARGEUR, HAUTEUR))
    
    bouton_piocher = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, HAUTEUR - 50), (100, 40)),
                                                    text='Piocher Pioche',
                                                    manager=manager)
    
    bouton_piocher_defausse = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((120, HAUTEUR - 50), (120, 40)),
                                                    text='Piocher Défausse',
                                                    manager=manager)
    
    bouton_defausser = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, HAUTEUR - 50), (100, 40)),
                                                    text='Défausser',
                                                    manager=manager)
    
    bouton_combiner = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((360, HAUTEUR - 50), (100, 40)),
                                                    text='Combiner',
                                                    manager=manager)

    cartes_selectionnees = []
    clock = pygame.time.Clock()
    
    while en_cours:
        time_delta = clock.tick(60)/1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
            
            if tour_joueur:
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    # Action du bouton "Piocher Pioche"
                    if event.ui_element == bouton_piocher and not a_pioche:
                        if not premier_tour:
                            carte_piochee = piocher(pioche, defausse)
                            mains["joueur"].append(carte_piochee)
                            trier_main_par_couleur_et_valeur(mains["joueur"])
                            a_pioche = True
                    
                    # Action du bouton "Piocher Défausse"
                    if event.ui_element == bouton_piocher_defausse and not a_pioche:
                        if not premier_tour and defausse:
                            carte_piochee = defausse.pop()
                            mains["joueur"].append(carte_piochee)
                            trier_main_par_couleur_et_valeur(mains["joueur"])
                            a_pioche = True
                    
                    # Action du bouton "Défausser"
                    if event.ui_element == bouton_defausser:
                        if cartes_selectionnees and (a_pioche or premier_tour):
                            carte_defaussee = cartes_selectionnees.pop()
                            mains["joueur"].remove(carte_defaussee)
                            defausse.append(carte_defaussee)
                            cartes_selectionnees.clear()
                            premier_tour = False
                            tour_joueur = False
                            a_pioche = False
                    
                    # Action du bouton "Combiner"
                    if event.ui_element == bouton_combiner:
                        if len(cartes_selectionnees) >= 3:
                            if est_suite(cartes_selectionnees) or est_groupe(cartes_selectionnees):
                                combinaisons.append(cartes_selectionnees.copy())
                                for carte in cartes_selectionnees:
                                    mains["joueur"].remove(carte)
                                cartes_selectionnees.clear()
                                print("Combinaison valide !")
                            else:
                                print("Combinaison non valide.")
                
                # Sélection des cartes avec un clic de souris
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for i, carte in enumerate(mains["joueur"]):
                        carte_rect = pygame.Rect(i * 80 + 10, HAUTEUR - 150, 71, 96)
                        if carte_rect.collidepoint(x, y):
                            if carte in cartes_selectionnees:
                                cartes_selectionnees.remove(carte)
                            else:
                                cartes_selectionnees.append(carte)
            
            manager.process_events(event)
        
        # Si le tour du joueur est terminé, l'ordinateur joue
        if not tour_joueur:
            tour_ordi(mains, defausse, combinaisons)
            tour_joueur = True  # Passe le tour au joueur
            
        manager.update(time_delta)
        afficher_interface(fenetre, mains, defausse, combinaisons)
        
        # Affiche une marque rouge sous chaque carte sélectionnée
        for i, carte in enumerate(mains["joueur"]):
            if carte in cartes_selectionnees:
                pygame.draw.rect(fenetre, ROUGE, (i * 80 + 10, HAUTEUR - 155, 71, 5))
        
        manager.draw_ui(fenetre)
        pygame.display.update()
        
        # Conditions de victoire
        if not mains["joueur"]:
            print("Félicitations ! Vous avez gagné la partie.")
            en_cours = False
        elif not mains["ordi"]:
            print("L'ordinateur a gagné la partie.")
            en_cours = False

    print("Partie terminée.")
    pygame.quit()

# Lance le jeu de Rami graphique
if __name__ == "__main__":
    jeu_rami_graphique()
