import random
import pygame
import os
import pygame_gui

class Carte:
    """
    Classe représentant une carte avec sa valeur et sa couleur.
    """
    symboles = {"♠": "s", "♥": "h", "♦": "d", "♣": "c", "J1": "JR", "J2": "JN"}
    noms_speciaux = {1: "A", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def get_nom(self):
        if self.couleur in ["J1", "J2"]:
            return self.couleur
        return self.noms_speciaux.get(self.valeur, str(self.valeur)) + self.symboles[self.couleur]

    def __str__(self):
        return f"{self.get_nom()}"

class Sabot:
    """
    Classe représentant un sabot contenant des cartes mélangées.
    """
    def __init__(self, chemin_images):
        self.cartes = []
        self.images_cartes = {}
        self.creer_jeu()
        self.charger_images(chemin_images)

    def creer_jeu(self):
        couleurs = ["♠", "♥", "♦", "♣"]
        for valeur in range(1, 14):
            for couleur in couleurs:
                self.cartes.append(Carte(valeur, couleur))
        self.cartes += [Carte(14, "J1"), Carte(14, "J2")]
        self.cartes *= 2  # Deux paquets
        random.shuffle(self.cartes)

    def charger_images(self, chemin_images):
        for carte in self.cartes:
            nom_carte = carte.get_nom()
            chemin_complet = os.path.join(chemin_images, f"{nom_carte}.gif")
            if os.path.exists(chemin_complet):
                self.images_cartes[(carte.valeur, carte.couleur)] = pygame.image.load(chemin_complet)

    def tirer_carte(self):
        return self.cartes.pop() if self.cartes else None

class JeuRamiGraphique:
    """
    Classe principale pour gérer une partie de Rami en mode graphique.
    """
    def __init__(self, largeur, hauteur, chemin_images):
        pygame.init()
        self.LARGEUR = largeur
        self.HAUTEUR = hauteur
        self.fenetre = pygame.display.set_mode((self.LARGEUR, self.HAUTEUR))
        pygame.display.set_caption("Jeu de Rami")
        self.sabot = Sabot(chemin_images)
        self.mains = {"joueur": [], "ordi": []}
        self.pioche = []
        self.defausse = []
        self.combinaisons = []
        self.cartes_selectionnees = []
        self.manager = pygame_gui.UIManager((self.LARGEUR, self.HAUTEUR))
        self.en_cours = True
        self.tour_joueur = True
        self.a_pioche = False
        self.init_ui()
        self.distribuer_cartes()

    def init_ui(self):
        self.bouton_piocher = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10, self.HAUTEUR - 50), (100, 40)),
            text='Piocher Pioche',
            manager=self.manager
        )
        self.bouton_piocher_defausse = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((120, self.HAUTEUR - 50), (120, 40)),
            text='Piocher Défausse',
            manager=self.manager
        )
        self.bouton_defausser = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((250, self.HAUTEUR - 50), (100, 40)),
            text='Défausser',
            manager=self.manager
        )
        self.bouton_combiner = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((360, self.HAUTEUR - 50), (100, 40)),
            text='Combiner',
            manager=self.manager
        )

    def distribuer_cartes(self):
        self.mains["joueur"] = [self.sabot.tirer_carte() for _ in range(15)]
        self.mains["ordi"] = [self.sabot.tirer_carte() for _ in range(14)]
        self.defausse.append(self.sabot.tirer_carte())
        self.pioche = self.sabot.cartes
        self.trier_main(self.mains["joueur"])

    def trier_main(self, main):
        main.sort(key=lambda carte: (carte.couleur, carte.valeur))

    def afficher_carte_graphique(self, carte, x, y, selectionnee=False):
        if (carte.valeur, carte.couleur) in self.sabot.images_cartes:
            self.fenetre.blit(self.sabot.images_cartes[(carte.valeur, carte.couleur)], (x, y))
        else:
            couleur = (255, 0, 0) if carte.couleur in ["♥", "♦"] else (0, 0, 0)
            pygame.draw.rect(self.fenetre, (255, 255, 255), (x, y, 71, 96))
            pygame.draw.rect(self.fenetre, couleur, (x, y, 71, 96), 2)
            font = pygame.font.Font(None, 24)
            texte = font.render(carte.get_nom(), True, couleur)
            self.fenetre.blit(texte, (x + 5, y + 35))
        if selectionnee:
            pygame.draw.rect(self.fenetre, (0, 255, 0), (x, y, 71, 96), 3)

    def afficher_main_graphique(self, main, y):
        for i, carte in enumerate(main):
            selectionnee = carte in self.cartes_selectionnees
            self.afficher_carte_graphique(carte, i * 80 + 10, y, selectionnee)

    def afficher_interface(self):
        self.fenetre.fill((0, 128, 0))
        self.afficher_main_graphique(self.mains["joueur"], self.HAUTEUR - 150)
        self.afficher_carte_graphique(self.defausse[-1], self.LARGEUR // 2 - 35, self.HAUTEUR // 2 - 48)
        
        # Afficher les combinaisons
        for i, combinaison in enumerate(self.combinaisons):
            for j, carte in enumerate(combinaison):
                self.afficher_carte_graphique(carte, j * 40 + 10, i * 110 + 10)
        
        font = pygame.font.Font(None, 36)
        texte = font.render(f"Cartes de l'ordinateur : {len(self.mains['ordi'])}", True, (255, 255, 255))
        self.fenetre.blit(texte, (10, 10))
        pygame.display.flip()

    def gerer_clic(self, x, y):
        for i, carte in enumerate(self.mains["joueur"]):
            carte_rect = pygame.Rect(i * 80 + 10, self.HAUTEUR - 150, 71, 96)
            if carte_rect.collidepoint(x, y):
                if carte in self.cartes_selectionnees:
                    self.cartes_selectionnees.remove(carte)
                else:
                    self.cartes_selectionnees.append(carte)

    def verifier_combinaison(self, cartes):
        if len(cartes) < 3:
            return False
        
        # Vérifier une suite
        if all(carte.couleur == cartes[0].couleur for carte in cartes):
            valeurs = sorted([carte.valeur for carte in cartes])
            if valeurs == list(range(min(valeurs), max(valeurs) + 1)):
                return True
        
        # Vérifier un brelan ou carré
        if len(set(carte.valeur for carte in cartes)) == 1:
            return True
        
        return False

    def combiner(self):
        if self.verifier_combinaison(self.cartes_selectionnees):
            self.combinaisons.append(self.cartes_selectionnees)
            for carte in self.cartes_selectionnees:
                self.mains["joueur"].remove(carte)
            self.cartes_selectionnees = []
        else:
            print("Combinaison invalide")

    def jouer(self):
        clock = pygame.time.Clock()
        while self.en_cours:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.en_cours = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.gerer_clic(x, y)
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.bouton_combiner:
                        self.combiner()

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.afficher_interface()
            self.manager.draw_ui(self.fenetre)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    chemin_images = r"C:\Mes codes\CDA_Codes\Algo_Python\Mini_app Objet\jeux\cartes"
    jeu = JeuRamiGraphique(1200, 768, chemin_images)
    jeu.jouer()
