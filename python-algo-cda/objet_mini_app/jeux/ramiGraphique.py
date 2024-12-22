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

class Carte:
    def __init__(self, valeur, couleur, image=None):
        self.valeur = valeur
        self.couleur = couleur
        self.image = image

    @property
    def nom_carte(self):
        if self.couleur == "J1":
            return "JR"  # Joker rouge
        elif self.couleur == "J2":
            return "JN"  # Joker noir
        symboles = {"♠": "s", "♥": "h", "♦": "d", "♣": "c"}
        noms_speciaux = {1: "A", 11: "J", 12: "Q", 13: "K"}
        return noms_speciaux.get(self.valeur, str(self.valeur)) + symboles[self.couleur]

    @property
    def est_joker(self):
        return self.valeur == 14

class Deck:
    def __init__(self, chemin_images):
        self.cartes = self.creer_jeu()
        self.images_cartes = self.charger_images_cartes(chemin_images)

    def creer_jeu(self):
        cartes = [Carte(valeur, couleur) for valeur in range(1, 14) for couleur in ["♠", "♥", "♦", "♣"]] * 2
        cartes += [Carte(14, "J1"), Carte(14, "J2")]  # Ajoute deux jokers
        random.shuffle(cartes)
        return cartes

    def charger_images_cartes(self, chemin_images):
        images = {}
        for carte in self.cartes:
            chemin_complet = os.path.join(chemin_images, f"{carte.nom_carte}.gif")
            if os.path.exists(chemin_complet):
                images[carte.nom_carte] = pygame.image.load(chemin_complet)
        return images

    def piocher(self):
        return self.cartes.pop() if self.cartes else None

    def reste(self):
        return len(self.cartes)

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def ajouter_carte(self, carte):
        if carte:
            self.main.append(carte)
            self.trier_main()

    def trier_main(self):
        self.main.sort(key=lambda carte: (carte.couleur, carte.valeur))

    def defausser_carte(self, index):
        if 0 <= index < len(self.main):
            return self.main.pop(index)

    def a_gagne(self):
        return not self.main

class JeuDeRami:
    def __init__(self):
        self.fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
        pygame.display.set_caption("Jeu de Rami")
        
        self.deck = Deck(r"C:\laragon\www\CDA\python-algo-cda\objet_mini_app\jeux\cartes")
        self.joueur = Joueur("Joueur")
        self.ordinateur = Joueur("Ordinateur")
        self.pioche = self.deck.cartes  # Utilise le deck pour la pioche
        self.defausse = [self.pioche.pop()]  # Place une carte de départ dans la défausse
        self.combinaisons = []
        self.manager = pygame_gui.UIManager((LARGEUR, HAUTEUR))
        self.boutons = self.creer_boutons()

        # Variables de contrôle de jeu
        self.tour_joueur = True
        self.premier_tour = True
        self.a_pioche = False
        self.cartes_selectionnees = []
        self.clock = pygame.time.Clock()
        
        self.distribuer_cartes()

    def distribuer_cartes(self):
        for _ in range(14):  # Distribue 14 cartes à chaque joueur
            self.joueur.ajouter_carte(self.pioche.pop())
            self.ordinateur.ajouter_carte(self.pioche.pop())
        self.joueur.ajouter_carte(self.pioche.pop())

    def creer_boutons(self):
        boutons = {}
        boutons['piocher_pioche'] = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10, HAUTEUR - 50), (100, 40)), text='Piocher Pioche', manager=self.manager)
        boutons['piocher_defausse'] = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((120, HAUTEUR - 50), (120, 40)), text='Piocher Défausse', manager=self.manager)
        boutons['defausser'] = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((250, HAUTEUR - 50), (100, 40)), text='Défausser', manager=self.manager)
        boutons['combiner'] = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((360, HAUTEUR - 50), (100, 40)), text='Combiner', manager=self.manager)
        boutons['ajouter_combinaison'] = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((470, HAUTEUR - 50), (150, 40)), text='Ajouter à Combinaison', manager=self.manager)
        return boutons

    def est_suite(self, cartes):
        cartes_non_jokers = sorted([c for c in cartes if not c.est_joker], key=lambda x: x.valeur)
        jokers = [c for c in cartes if c.est_joker]
        jokers_restants = len(jokers)

        # Vérifie que toutes les cartes non-jokers sont de la même couleur
        couleurs = {carte.couleur for carte in cartes_non_jokers}
        if len(couleurs) != 1:
            return False

        # Vérifie la séquence de valeurs avec jokers pour combler les trous
        valeurs = [carte.valeur for carte in cartes_non_jokers]
        for i in range(len(valeurs) - 1):
            difference = valeurs[i + 1] - valeurs[i]
            if difference > 1:
                jokers_a_utiliser = difference - 1
                if jokers_a_utiliser > jokers_restants:
                    return False
                jokers_restants -= jokers_a_utiliser

        return True

    def est_groupe(self, cartes):
        cartes_non_jokers = [c for c in cartes if not c.est_joker]
        jokers = [c for c in cartes if c.est_joker]

        valeurs = {carte.valeur for carte in cartes_non_jokers}
        return len(valeurs) == 1 and (len(cartes_non_jokers) + len(jokers)) >= 3

    def peut_ajouter_a_combinaison(self, carte, combinaison):
        if self.est_suite(combinaison + [carte]):
            return True
        if self.est_groupe(combinaison + [carte]):
            return True
        return False

    def afficher_cartes(self):
        for i, carte in enumerate(self.joueur.main):
            pos_x, pos_y = i * 80 + 10, HAUTEUR - 150
            if carte.nom_carte in self.deck.images_cartes:
                self.fenetre.blit(self.deck.images_cartes[carte.nom_carte], (pos_x, pos_y))
            else:
                pygame.draw.rect(self.fenetre, BLANC, (pos_x, pos_y, 71, 96))
                pygame.draw.rect(self.fenetre, NOIR, (pos_x, pos_y, 71, 96), 2)
            
            if carte in self.cartes_selectionnees:
                pygame.draw.rect(self.fenetre, ROUGE, (pos_x, pos_y, 71, 96), 3)

        if self.defausse:
            carte = self.defausse[-1]
            pos_x, pos_y = LARGEUR // 2 - 35, HAUTEUR // 2 - 48
            if carte.nom_carte in self.deck.images_cartes:
                self.fenetre.blit(self.deck.images_cartes[carte.nom_carte], (pos_x, pos_y))
            else:
                pygame.draw.rect(self.fenetre, BLANC, (pos_x, pos_y, 71, 96))
                pygame.draw.rect(self.fenetre, NOIR, (pos_x, pos_y, 71, 96), 2)

        for idx, combinaison in enumerate(self.combinaisons):
            for j, carte in enumerate(combinaison):
                pos_x, pos_y = 10 + j * 40, 100 + idx * 100
                if carte.nom_carte in self.deck.images_cartes:
                    self.fenetre.blit(self.deck.images_cartes[carte.nom_carte], (pos_x, pos_y))
                else:
                    pygame.draw.rect(self.fenetre, BLANC, (pos_x, pos_y, 71, 96))
                    pygame.draw.rect(self.fenetre, NOIR, (pos_x, pos_y, 71, 96), 2)

    def afficher_interface(self):
        self.fenetre.fill(VERT)
        self.afficher_cartes()

        font = pygame.font.Font(None, 36)
        texte_joueur = font.render(f"Cartes du Joueur : {len(self.joueur.main)}", True, BLANC)
        self.fenetre.blit(texte_joueur, (10, HAUTEUR - 180))
        
        texte_ordi = font.render(f"Cartes de l'Ordinateur : {len(self.ordinateur.main)}", True, BLANC)
        self.fenetre.blit(texte_ordi, (10, 10))
        
        pygame.display.flip()

    def gestion_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, carte in enumerate(self.joueur.main):
                    carte_rect = pygame.Rect(i * 80 + 10, HAUTEUR - 150, 71, 96)
                    if carte_rect.collidepoint(x, y):
                        if carte in self.cartes_selectionnees:
                            self.cartes_selectionnees.remove(carte)
                        else:
                            self.cartes_selectionnees.append(carte)
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.boutons['piocher_pioche'] and not self.a_pioche and not self.premier_tour:
                    self.joueur.ajouter_carte(self.pioche.pop())
                    self.a_pioche = True
                elif event.ui_element == self.boutons['piocher_defausse'] and not self.a_pioche and not self.premier_tour:
                    if self.defausse:
                        self.joueur.ajouter_carte(self.defausse.pop())
                        self.a_pioche = True
                elif event.ui_element == self.boutons['defausser'] and (self.a_pioche or self.premier_tour):
                    if self.cartes_selectionnees:
                        carte_defaussee = self.joueur.defausser_carte(self.joueur.main.index(self.cartes_selectionnees.pop()))
                        if carte_defaussee:
                            self.defausse.append(carte_defaussee)
                        self.a_pioche = False
                        self.premier_tour = False
                        self.tour_joueur = False
                elif event.ui_element == self.boutons['combiner']:
                    if len(self.cartes_selectionnees) >= 3:
                        if self.est_suite(self.cartes_selectionnees) or self.est_groupe(self.cartes_selectionnees):
                            self.combinaisons.append(self.cartes_selectionnees.copy())
                            for carte in self.cartes_selectionnees:
                                self.joueur.main.remove(carte)
                            self.cartes_selectionnees.clear()
                            print("Combinaison valide ajoutée.")
                        else:
                            print("Combinaison non valide.")
                elif event.ui_element == self.boutons['ajouter_combinaison']:
                    if len(self.cartes_selectionnees) == 1:
                        carte = self.cartes_selectionnees[0]
                        ajout_effectue = False
                        for combinaison in self.combinaisons:
                            if self.peut_ajouter_a_combinaison(carte, combinaison):
                                combinaison.append(carte)
                                self.joueur.main.remove(carte)
                                ajout_effectue = True
                                print("Carte ajoutée à une combinaison existante.")
                                break
                        if not ajout_effectue:
                            print("Impossible d'ajouter cette carte à une combinaison.")
                        self.cartes_selectionnees.clear()
            self.manager.process_events(event)
        return True

    def tour_ordinateur(self):
        carte_piochee = self.pioche.pop()
        if carte_piochee:
            self.ordinateur.ajouter_carte(carte_piochee)
            self.defausse.append(self.ordinateur.defausser_carte(random.randint(0, len(self.ordinateur.main) - 1)))

    def jeu(self):
        en_cours = True
        while en_cours:
            en_cours = self.gestion_evenements()
            
            if not self.tour_joueur:
                self.tour_ordinateur()
                self.tour_joueur = True

            self.manager.update(self.clock.tick(60) / 1000.0)
            self.afficher_interface()
            self.manager.draw_ui(self.fenetre)
            pygame.display.update()
            
            if self.joueur.a_gagne():
                print("Félicitations ! Vous avez gagné la partie.")
                en_cours = False
            elif self.ordinateur.a_gagne():
                print("L'ordinateur a gagné la partie.")
                en_cours = False

        pygame.quit()

if __name__ == "__main__":
    jeu = JeuDeRami()
    jeu.jeu()
