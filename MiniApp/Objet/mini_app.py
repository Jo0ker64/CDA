# Importer les modules contenant les jeux
from jeux.CalculRemise import CalculRemise  # Fonction pour calculer une remise
from jeux.JeuDeDes import JeuDeDes  # Jeu de lancé de dés
from jeux.JustePrix import JustePrix  # Jeu du juste prix
from jeux.HorlogeNumerique import HorlogeNumerique  # Horloge numérique qui affiche HH:MM:SS
from jeux.JeuDuPendu import JeuDuPendu  # Jeu du pendu
from jeux.CodeDeCésar import CodeurDecodeurCesar  # Déchiffreur basé sur le code César
from jeux.GestionnaireDeContact import contact  # Gestionnaire de contacts
from jeux.Chifoumi import ChifoumiSheldon  # Jeu de pierre-feuille-ciseaux
from jeux.Morpion import Morpion  # Jeu du morpion
from jeux.Démineur import démineur  # Jeu de démineur
from jeux.Mastermind import Mastermind  # Jeu du mastermind
from jeux.CodeMorse import MorseCode  # Traducteur en code Morse
from jeux.JeuDesAllumettes import JeuDesAllumettes  # Jeu des allumettes
from jeux.BatailleNavale import BatailleNavale  # Jeu de bataille navale
from jeux.BlackJack import BlackJack  # Jeu de BlackJack
from jeux.Rami import Rami  # Jeu de Rami
from jeux.RamiGraphique import JeuRamiGraphique  # Jeu de Rami avec interface graphique
from jeux.Snake import SnakeGame  # Jeu de Snake
from jeux.Uno import PartieUno  # Jeu de Uno


class MiniApp:
    """Classe principale pour gérer l'application et son menu."""

    def __init__(self):
        """Initialise l'application."""
        self.choix = None  # Variable pour stocker le choix de l'utilisateur

    @staticmethod
    def affiche_menu():
        """Affiche le menu principal à l'utilisateur et retourne son choix."""
        print("**************************************")
        print("Menu de l'application :")
        print("0. Quitter")  # Option pour quitter l'application
        print("1. Calculer une remise en %")  # Appelle le module pour calculer une remise
        print("2. Lancé de dé")  # Appelle le jeu de dés
        print("3. Jeu du juste prix")  # Appelle le jeu du juste prix
        print("4. Horloge numérique (HH:MM:SS qui défile)")  # Affiche une horloge numérique
        print("5. Jeu du pendu")  # Appelle le jeu du pendu
        print("6. Décodeur César")  # Appelle le décodeur basé sur le code César
        print("7. Gestionnaire de contact")  # Appelle le gestionnaire de contacts
        print("8. Chifoumi Sheldon")  # Appelle le jeu de pierre-feuille-ciseaux
        print("9. Morpion")  # Appelle le jeu du morpion
        print("10. Démineur")  # Appelle le jeu de démineur
        print("11. Mastermind")  # Appelle le jeu de mastermind
        print("12. Code morse")  # Appelle le traducteur en code Morse
        print("13. Allumettes")  # Appelle le jeu des allumettes
        print("14. Bataille navale")  # Appelle le jeu de bataille navale
        print("15. BlackJack")  # Appelle le jeu de BlackJack
        print("16. Rami")  # Appelle le jeu de Rami
        print("17. Rami graphique")  # Appelle le jeu de Rami avec interface graphique
        print("18. Snake")  # Appelle le jeu de Snake
        print("19. Uno")  # Appelle le jeu de Uno
        print("**************************************")
        return input("Votre choix : ")  # Retourne le choix de l'utilisateur sous forme de chaîne

    def lancer_action(self, choix):
        """Exécute l'action correspondant au choix de l'utilisateur."""
        match choix:
            # Appel dans le mini_app.py, dans la méthode `lancer_action` :
            case "1":
                montant = float(input('Entrez le montant de l\'article : '))
                remise = float(input('Entrez le pourcentage de remise : '))
                CalculRemise.calculer(montant, remise)
            case "2":  # Jeu de dés
                jeu = JeuDeDes()  # Crée une instance du jeu de dés
                jeu.jouer()  # Lance le jeu
            case "3":  # Jeu du juste prix
                jeu = JustePrix()  # Crée une instance du jeu Juste Prix
                jeu.jouer()  # Lance le jeu
            case "4":  # Horloge numérique
                horloge = HorlogeNumerique(duree_affichage=10)  # Crée une instance avec une durée d'affichage de 10 secondes
                horloge.afficher_horloge()
            case "5":  # Jeu du pendu
                jeu = JeuDuPendu()  # Crée une instance du jeu du pendu
                jeu.jouer()
            case "6":  # Décodeur César
                cesar = CodeurDecodeurCesar()  # Crée une instance de la classe
                cesar.lancer()  # Lance le programme interactif
            case "7":  # Gestionnaire de contacts
                contact()
            case "8":  # Jeu de Chifoumi
                jeu = ChifoumiSheldon()  # Crée une instance du jeu
                jeu.jouer()
            case "9":  # Jeu du Morpion
                jeu = Morpion()  # Crée une instance du jeu de Morpion
                jeu.jouer()
            case "10":  # Jeu de Démineur
                démineur()
            case "11":  # Jeu de Mastermind
                jeu = Mastermind()  # Crée une instance du jeu Mastermind
                jeu.jouer()
            case "12":  # Traducteur en code Morse
                morse = MorseCode()  # Crée une instance de la classe
                morse.interaction()
            case "13":  # Jeu des Allumettes
                jeu = JeuDesAllumettes()  # Crée une instance du jeu
                jeu.jouer()
            case "14":  # Jeu de Bataille navale
                jeu = BatailleNavale()  # Crée une instance du jeu
                jeu.jouer()  # Lance le jeu
            case "15":  # Jeu de BlackJack
                jeu = BlackJack()
                jeu.jouer()
            case "16":  # Jeu de Rami
                jeu = Rami()
                jeu.jouer()
            case "17":  # Jeu de Rami graphique
                chemin_images = r"C:\Mes codes\CDA_Codes\Algo_Python\Mini_app Objet\jeux\cartes"
                jeu = JeuRamiGraphique(1200, 768, chemin_images)
                jeu.jouer()
            case "18":  # Jeu de Snake
                game = SnakeGame()
                game.run()
            case "19":  # Jeu de Uno
                partie = PartieUno()
                partie.lancer_partie()
            case _:  # Gestion des choix invalides
                print("Choix invalide, veuillez réessayer.")  # Message d'erreur si le choix est incorrect

    def run(self):
        """Démarre l'application et affiche le menu jusqu'à ce que l'utilisateur quitte."""
        while self.choix != "0":  # Boucle principale, continue jusqu'à ce que l'utilisateur choisisse "0"
            self.choix = self.affiche_menu()  # Afficher le menu et récupérer le choix
            if self.choix != "0":  # Si l'utilisateur ne choisit pas de quitter
                self.lancer_action(self.choix)  # Exécuter l'action associée au choix
        print("*** FIN DU PROGRAMME ***")  # Message affiché lorsque le programme se termine


# Point d'entrée du programme
if __name__ == "__main__":
    app = MiniApp()  # Crée une instance de l'application
    app.run()  # Exécute l'application
