print("Lancement de l'horloge numérique ...")
import time

from datetime import datetime, timedelta

# importer uniquement le système à partir du système d'exploitation
from os import system, name

# définir notre fonction effacer écran
def clear():

    # pour windows
    if name == 'nt':
        _ = system('cls')

    # pour mac & linux(ici, os.name est 'posix')
    else:
        _ = system('clear')

def horloge():
    # Obtenez l'heure actuelle au lancement du script
    heure_initiale = datetime.now()
    print("Heure de départ:", heure_initiale.strftime("%H:%M:%S")) # strftime = string-format-time

    # Durée pour l'affichage de l'horloge (en secondes)
    duree_affichage = 10  # exemple : XX secondes

    # Boucle tant que
    while True:
        heure_actuelle = datetime.now() # variable = class.metode
        temps_ecoule = (heure_actuelle - heure_initiale).total_seconds()
        
        # Afficher l'heure qui défile sans mise à jour en temps réel
        heure_defilante = (heure_initiale + timedelta(seconds=temps_ecoule)).strftime("%H:%M:%S")
        print("Heure actuelle:", heure_defilante)
        
        if temps_ecoule >= duree_affichage:
            print("Fin de l'horloge.")
            break
        
        # Pause pour ne pas réactualiser en continu
        time.sleep(1)

        # appelle la fonction clear pour effacer l'ecran et eviter repetition en saut de ligne
        clear()
if __name__ == "__main__":
    horloge()



#########################  CORRECTION 

"""
Horloge numérique simple affichant l'heure pendant une durée définie.
"""
# import time
# from datetime import datetime, timedelta
# from os import system, name

# # Constantes
# DUREE_AFFICHAGE = 10  # en secondes

# def clear():
#     """Efface l'écran du terminal."""
#     system('cls' if name == 'nt' else 'clear')

# def horloge():
#     """Affiche une horloge numérique pendant une durée définie."""
#     heure_initiale = datetime.now()
#     print(f"Heure de départ: {heure_initiale.strftime('%H:%M:%S')}")

#     while True:
#         heure_actuelle = datetime.now()
#         temps_ecoule = (heure_actuelle - heure_initiale).total_seconds()
        
#         heure_defilante = (heure_initiale + timedelta(seconds=temps_ecoule)).strftime("%H:%M:%S")
#         print(f"Heure actuelle: {heure_defilante}")
        
#         if temps_ecoule >= DUREE_AFFICHAGE:
#             print("Fin de l'horloge.")
#             break
        
#         time.sleep(1)
#         clear()

# if __name__ == "__main__":
#     horloge()

