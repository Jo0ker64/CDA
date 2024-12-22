import random

class JeuDeDes:
    def __init__(self):
        """
        Initialise le jeu avec un score total de zéro et aucun lancer effectué.
        """
        self.score_total = 0
        self.nombre_lancers = 0

    def lancer_de(self, nombre_faces):
        """
        Simule le lancer d'un dé avec un nombre spécifique de faces.
        
        :param nombre_faces: Le nombre de faces du dé
        :return: Un nombre aléatoire entre 1 et nombre_faces
        """
        return random.randint(1, nombre_faces)

    def jouer(self):
        """
        Démarre le jeu de dés, permet à l'utilisateur de lancer les dés, 
        de visualiser les résultats et de décider s'il souhaite continuer ou non.
        """
        print("Bienvenue au jeu de dés !")
        
        while True:
            # Demande à l'utilisateur le nombre de faces du dé, utilise 6 faces par défaut si entrée vide
            nombre_faces_input = input("Combien de faces voulez-vous pour votre dé ? (6 par défaut) ")
            nombre_faces = 6 if nombre_faces_input == "" else int(nombre_faces_input)
            
            # Demande le nombre de dés à lancer
            nombre_des = int(input("Combien de dés voulez-vous lancer ? "))
            
            # Lancement des dés
            resultats = self.lancer_plusieurs_des(nombre_des, nombre_faces)
            
            # Calcul et affichage du total pour ce lancer
            total_lancer = sum(resultats)
            print(f"Total de ce lancer: {total_lancer}")
            
            # Mise à jour du score total et du nombre de lancers
            self.score_total += total_lancer
            self.nombre_lancers += 1
            
            # Affichage du score total actuel
            print(f"Score total actuel: {self.score_total}")
            
            # Demande si l'utilisateur veut continuer à jouer
            if not self.rejouer():
                break
        
        # Affichage des statistiques finales
        self.afficher_statistiques_finales()

    def lancer_plusieurs_des(self, nombre_des, nombre_faces):
        """
        Lance plusieurs dés et affiche chaque résultat.
        
        :param nombre_des: Le nombre de dés à lancer
        :param nombre_faces: Le nombre de faces pour chaque dé
        :return: Liste des résultats pour chaque dé lancé
        """
        resultats = []
        for i in range(nombre_des):
            resultat = self.lancer_de(nombre_faces)
            resultats.append(resultat)
            print(f"Dé {i + 1}: {resultat}")
        return resultats

    def rejouer(self):
        """
        Demande à l'utilisateur s'il souhaite relancer les dés.
        
        :return: True si l'utilisateur souhaite continuer, sinon False
        """
        rejouer = input("Voulez-vous relancer les dés ? (O/N) ")
        return rejouer.lower() == 'o'

    def afficher_statistiques_finales(self):
        """
        Affiche le nombre total de lancers, le score total et la moyenne par lancer.
        """
        print("\n--- Résultat final ---")
        print(f"Nombre total de lancers: {self.nombre_lancers}")
        print(f"Score total: {self.score_total}")
        
        # Calcul et affichage de la moyenne par lancer
        if self.nombre_lancers > 0:
            moyenne = self.score_total / self.nombre_lancers
            print(f"Moyenne par lancer: {moyenne:.2f}")
        print("Merci d'avoir joué !")

# Point d'entrée du programme
if __name__ == "__main__":
    jeu = JeuDeDes()
    jeu.jouer()
