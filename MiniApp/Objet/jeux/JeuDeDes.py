import random

class JeuDeDes:
    """
    Classe pour gérer le jeu de dés.
    """

    def __init__(self):
        """
        Initialise les variables nécessaires pour suivre le score total
        et le nombre de lancers.
        """
        self.score_total = 0  # Score total accumulé
        self.nombre_lancers = 0  # Nombre de lancers effectués

    def lancer_de(self, nombre_faces):
        """
        Simule le lancer d'un dé avec un nombre spécifique de faces.

        :param nombre_faces: int, le nombre de faces du dé.
        :return: int, un nombre aléatoire entre 1 et nombre_faces.
        """
        return random.randint(1, nombre_faces)

    def jouer(self):
        """
        Méthode principale pour exécuter le jeu de dés.
        """
        print("Bienvenue au jeu de dés !")

        while True:
            # Demande à l'utilisateur le nombre de faces du dé
            nombre_faces_input = input("Combien de faces voulez-vous pour votre dé ? (6 par défaut) ")
            nombre_faces = 6 if nombre_faces_input == "" else int(nombre_faces_input)  # Par défaut 6 faces

            # Demande le nombre de dés à lancer
            nombre_des = int(input("Combien de dés voulez-vous lancer ? "))

            # Liste pour stocker les résultats des lancers
            resultats = []
            for i in range(nombre_des):
                resultat = self.lancer_de(nombre_faces)
                resultats.append(resultat)
                print(f"Dé {i + 1}: {resultat}")

            # Calcul du total pour ce lancer
            total_lancer = sum(resultats)
            print(f"Total de ce lancer: {total_lancer}")

            # Mise à jour du score total et du nombre de lancers
            self.score_total += total_lancer
            self.nombre_lancers += 1

            # Affichage du score total actuel
            print(f"Score total actuel: {self.score_total}")

            # Demande si l'utilisateur veut continuer à jouer
            rejouer = input("Voulez-vous relancer les dés ? (O/N) ")
            if rejouer.lower() != 'o':  # Quitte la boucle si l'utilisateur ne veut plus jouer
                break

        # Affiche les statistiques finales
        self.afficher_resultats()

    def afficher_resultats(self):
        """
        Affiche les résultats finaux du jeu, y compris les statistiques.
        """
        print("\n--- Résultat final ---")
        print(f"Nombre total de lancers: {self.nombre_lancers}")
        print(f"Score total: {self.score_total}")

        # Calcul et affichage de la moyenne par lancer si au moins un lancer a été effectué
        if self.nombre_lancers > 0:
            moyenne = self.score_total / self.nombre_lancers
            print(f"Moyenne par lancer: {moyenne:.2f}")

        print("Merci d'avoir joué !")


# Exemple d'utilisation autonome
if __name__ == "__main__":
    jeu = JeuDeDes()  # Crée une instance de la classe JeuDeDes
    jeu.jouer()  # Lance le jeu
