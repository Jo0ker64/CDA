# Importer les fichiers
# from nomDuDossier.mon_document import le ou les éléments que je souhaites utilisé

from fonction_jeux.remise import calcul_remise
from fonction_jeux.dés import des
from fonction_jeux.prix import juste_prix
from fonction_jeux.horloge import horloge
from fonction_jeux.pendu import pendu
from fonction_jeux.cesar import cesar
from fonction_jeux.contact import contact
from fonction_jeux.chifoumi import chifoumi
from fonction_jeux.morpion import morpion
from fonction_jeux.démineur import démineur
from fonction_jeux.mastermind import mastermind
from fonction_jeux.morse import code_morse
from fonction_jeux.allumette import allumette
from fonction_jeux.bataille import bataille_navale
# from fonction_jeux.  import 
# from fonction_jeux.  import 



# Définition de la fonction pour afficher le menu principal
def affiche_menu():
    # Affichage du menu avec différentes options
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
    print("15. ")
    print("16. ")

    print("**************************************")
    # Demande à l'utilisateur de faire un choix et retourne ce choix
    return input("Votre choix : ")

# Affichage initial du menu et récupération du choix de l'utilisateur
choix = affiche_menu()


# Boucle principale du programme
while choix != "0":
    # Utilisation de l'instruction match pour gérer les différents choix
    match (choix):
        case "1":
            # Calcul de remise
            montant = int(input('Montant : '))
            remise = int(input('La remise : '))
            calcul_remise(montant, remise)
        case "2":
            # Jeu de dés
            des()
        case "3":
            # Jeu du juste prix
            juste_prix()
        case "4":
            # Horloge numérique
            horloge()
        case "5":
            # Jeu du pendu
            pendu()
        case "6":
            # Décodeur César
            cesar()
        case "7":
            # Gestionnaire de contact
            contact()
        case "8":
            #chifoumi
            chifoumi()
        case "9":
            #morpion
            morpion()
        case  "10":
            #démineur
            démineur()
        case "11":
            #code morse
            mastermind()
        case "12":
            #code morse
            code_morse()
        case "13":
            #allumette
            allumette()
        case "14":
            # bataille navale
            bataille_navale()
        # case "15":
        #     #
        # case "16":
        #     #



    # Réaffichage du menu après chaque action
    choix = affiche_menu()

# Message de fin de programme
print("*** FIN DU PROGRAMME ***")
