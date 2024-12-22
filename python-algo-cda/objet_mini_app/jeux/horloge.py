import time  # Importation du module time pour gérer les pauses
from datetime import datetime, timedelta  # Importation de datetime et timedelta pour gérer le temps et les intervalles
from os import system, name  # Importation de fonctions pour interagir avec le système d'exploitation

class HorlogeNumerique:
    """
    Classe pour afficher une horloge numérique pendant une durée définie.
    """

    def __init__(self, duree_affichage=10):
        """
        Initialise l'horloge avec la durée pendant laquelle elle doit s'afficher.

        :param duree_affichage: Durée d'affichage de l'horloge en secondes
        """
        # Stocke la durée d'affichage en secondes
        self.duree_affichage = duree_affichage

    def clear(self):
        """
        Efface l'écran du terminal en fonction du système d'exploitation.
        """
        # Si le système est Windows, utilise la commande 'cls' pour effacer l'écran
        if name == 'nt':
            _ = system('cls')
        # Sinon, pour Mac et Linux, utilise la commande 'clear'
        else:
            _ = system('clear')

    def lancer_horloge(self):
        """
        Lance l'affichage de l'horloge numérique pendant la durée définie.
        """
        # Stocke l'heure de départ (moment où l'horloge démarre)
        heure_initiale = datetime.now()
        print("Heure de départ:", heure_initiale.strftime("%H:%M:%S"))  # Affiche l'heure de départ au format HH:MM:SS

        # Boucle qui continue jusqu'à ce que la durée d'affichage soit atteinte
        while True:
            # Récupère l'heure actuelle pour chaque cycle de boucle
            heure_actuelle = datetime.now()
            # Calcule le temps écoulé en secondes depuis le début
            temps_ecoule = (heure_actuelle - heure_initiale).total_seconds()
            
            # Calcule l'heure qui défile en ajoutant le temps écoulé à l'heure initiale
            heure_defilante = (heure_initiale + timedelta(seconds=temps_ecoule)).strftime("%H:%M:%S")
            # Affiche l'heure actuelle formatée
            print("Heure actuelle:", heure_defilante)
            
            # Vérifie si la durée d'affichage est atteinte
            if temps_ecoule >= self.duree_affichage:
                # Si oui, affiche un message de fin et arrête la boucle
                print("Fin de l'horloge.")
                break
            
            # Pause de 1 seconde pour éviter une mise à jour trop rapide
            time.sleep(1)
            # Efface l'écran pour éviter d'accumuler les lignes d'affichage
            self.clear()

# Point d'entrée du programme
if __name__ == "__main__":
    # Crée une instance de HorlogeNumerique avec une durée d'affichage de 10 secondes
    horloge = HorlogeNumerique(duree_affichage=10)
    # Lance l'horloge numérique
    horloge.lancer_horloge()
