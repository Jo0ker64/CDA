from jeux.remise import calcul_remise
from jeux.dés import des
from jeux.prix import juste_prix
from jeux.horloge import horloge
from jeux.pendu import pendu
from jeux.cesar import cesar
from jeux.contact import contact
from jeux.chifoumi import chifoumi
from jeux.morpion import morpion
from jeux.démineur import démineur
from jeux.mastermind import mastermind
from jeux.morse import code_morse
from jeux.allumette import allumette
from jeux.bataille import bataille_navale

class ApplicationJeux:
    def __init__(self):
        self.choix = None
    
    def affiche_menu(self):
        print("**************************************")
        print("Menu de l'application :")
        print("0. Quitter")
        print("1. Calculer une remise en %")
        print("2. Lancé de dé")
        print("3. Jeu du juste prix")
        print("4. Horloge numérique (HH:MM:SS qui défile)")
        print("5. Jeu du pendu")
        print("6. Décodeur César")
        print("7. Gestionnaire de contact")
        print("8. Chifoumi Sheldon")
        print("9. Morpion")
        print("10. Démineur")
        print("11. Mastermind")
        print("12. Code morse")
        print("13. Allumettes")
        print("14. Bataille navale")
        print("**************************************")
        self.choix = input("Votre choix : ")

    def lancer_application(self):
        while self.choix != "0":
            self.executer_choix()
            self.affiche_menu()
        print("*** FIN DU PROGRAMME ***")

    def executer_choix(self):
        match self.choix:
            case "1":
                montant = int(input('Montant : '))
                remise = int(input('La remise : '))
                calcul_remise(montant, remise)
            case "2":
                des()
            case "3":
                juste_prix()
            case "4":
                horloge()
            case "5":
                pendu()
            case "6":
                cesar()
            case "7":
                contact()
            case "8":
                chifoumi()
            case "9":
                morpion()
            case "10":
                démineur()
            case "11":
                mastermind()
            case "12":
                code_morse()
            case "13":
                allumette()
            case "14":
                bataille_navale()
            # case "15" et "16" peuvent être ajoutés ici

if __name__ == "__main__":
    app = ApplicationJeux()
    app.affiche_menu()
    app.lancer_application()
