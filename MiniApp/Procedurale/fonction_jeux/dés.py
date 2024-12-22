print("Lancé de dé ...")

import random

# Fonction pour simuler le lancer d'un dé
def lancer_de(nombre_faces):
    """ 
    Simule le lancer d'un dé avec un nombre spécifique de faces.
    :param nombre_faces: Le nombre de faces du dé
    :return: Un nombre aléatoire entre 1 et nombre_faces
    """
    return random.randint(1, nombre_faces)

# Fonction principale du jeu de dés
def des():
    print("Bienvenue au jeu de dés !")
    
    # Initialisation des variables pour le score
    score_total = 0
    nombre_lancers = 0

    #BOUCLE TANT QUE 
    while True:
        # Demande à l'utilisateur le nombre de faces du dé
        nombre_faces_input = input("Combien de faces voulez-vous pour votre dé ? (6 par défaut) ")
        # Utilise 6 faces par défaut si l'entrée est vide
        nombre_faces = 6 if nombre_faces_input == "" else int(nombre_faces_input)
        
        # Demande le nombre de dés à lancer
        nombre_des = int(input("Combien de dés voulez-vous lancer ? "))
        
        # Lancement des dés et stockage des résultats
        resultats = []
        # BOUCLE RÉPÉTITIONS POUR
        for i in range(nombre_des):
            resultat = lancer_de(nombre_faces)
            resultats.append(resultat)
            print(f"Dé {i+1}: {resultat}")
        
        # Calcul et affichage du total pour ce lancer
        total_lancer = sum(resultats)
        print(f"Total de ce lancer: {total_lancer}")
        
        # Mise à jour du score total et du nombre de lancers
        score_total += total_lancer
        nombre_lancers += 1
        
        # Affichage du score total actuel
        print(f"Score total actuel: {score_total}")
        
        # Demande si l'utilisateur veut continuer à jouer
        rejouer = input("Voulez-vous relancer les dés ? (O/N) ")
        if rejouer.lower() != 'o':
            break
    
    # Affichage des statistiques finales
    print("\n--- Résultat final ---")
    print(f"Nombre total de lancers: {nombre_lancers}")
    print(f"Score total: {score_total}")
    # Calcul et affichage de la moyenne par lancer
    if nombre_lancers > 0:
        moyenne = score_total / nombre_lancers
        print(f"Moyenne par lancer: {moyenne:.2f}")
    print("Merci d'avoir joué !")

# Point d'entrée du programme
if __name__ == "__main__":
    des()
