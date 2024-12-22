import time
from datetime import datetime, timedelta
from os import system, name

class HorlogeNumerique:
    """
    Classe représentant une horloge numérique simple affichant l'heure
    pendant une durée définie.
    """

    def __init__(self, duree_affichage=10):
        """
        Initialise les paramètres de l'horloge.

        :param duree_affichage: int, durée en secondes pendant laquelle l'horloge sera affichée.
        """
        self.duree_affichage = duree_affichage  # Durée d'affichage en secondes
        self.heure_initiale = datetime.now()  # Heure de départ

    @staticmethod
    def clear():
        """
        Efface l'écran du terminal pour un affichage propre.
        Compatible avec Windows, MacOS et Linux.
        """
        # Utilise la commande appropriée selon le système d'exploitation
        system('cls' if name == 'nt' else 'clear')

    def afficher_horloge(self):
        """
        Affiche l'horloge numérique pendant la durée spécifiée.
        """
        print(f"Heure de départ : {self.heure_initiale.strftime('%H:%M:%S')}")

        # Boucle principale pour afficher l'horloge
        while True:
            heure_actuelle = datetime.now()  # Heure actuelle
            temps_ecoule = (heure_actuelle - self.heure_initiale).total_seconds()  # Temps écoulé en secondes

            # Calcule et formatte l'heure qui défile
            heure_defilante = (self.heure_initiale + timedelta(seconds=temps_ecoule)).strftime("%H:%M:%S")
            print(f"Heure actuelle : {heure_defilante}")

            # Vérifie si la durée d'affichage est écoulée
            if temps_ecoule >= self.duree_affichage:
                print("Fin de l'horloge.")
                break

            # Pause d'une seconde pour éviter un rafraîchissement constant
            time.sleep(1)

            # Efface l'écran avant la prochaine mise à jour
            self.clear()


# Exemple d'utilisation autonome
if __name__ == "__main__":
    horloge = HorlogeNumerique(duree_affichage=10)  # Crée une instance avec une durée d'affichage de 10 secondes
    horloge.afficher_horloge()  # Lance l'affichage de l'horloge
