# Votre script demande une chaine de caractères en entrée et vous l’affichez dans le sens inverse

#################################################################################################
        # Demande à l'utilisateur d'entrer une chaîne de caractères
        # La fonction input() récupère la saisie de l'utilisateur et la stocke dans la variable 'chaine'
# chaine = input("Entrez une chaîne de caractères : ")

        # Inverse la chaîne de caractères
        # [::-1] est une technique de découpage (slicing) en Python :
        #   - Le premier ':' indique qu'on prend toute la chaîne
        #   - Le deuxième ':' indique qu'on ne spécifie pas de fin
        #   - '-1' est le pas, qui indique qu'on parcourt la chaîne de la fin vers le début
# chaine_inverse = chaine[::-1]

        # Affiche la chaîne inversée
        # La fonction print() est utilisée pour afficher le résultat
        # La virgule après la chaîne "Chaîne inversée :" ajoute automatiquement un espace avant d'afficher chaine_inverse
# print("Chaîne inversée :", chaine_inverse)
#################################################################################################

#################################################################################################
        # Demande à l'utilisateur d'entrer une chaîne de caractères
        # La fonction input() récupère la saisie de l'utilisateur et la stocke dans la variable 'chaine'
# chaine = input("Entrez une chaîne de caractères : ")

        # Initialise une chaîne vide pour stocker le résultat inversé
# chaine_inversee = ""

        # Initialise l'index à la dernière position de la chaîne
        # len(chaine) donne la longueur de la chaîne, on soustrait 1 car les indices commencent à 0
#index = len(chaine) - 1

        # Boucle while qui s'exécute tant que l'index est supérieur ou égal à 0
#while index >= 0:
        # Ajoute le caractère à la position 'index' de 'chaine' à la fin de 'chaine_inversee'
    #chaine_inversee += chaine[index]
        # Décrémente l'index pour passer au caractère précédent
    #index -= 1

        # Affiche la chaîne inversée
        # La fonction print() est utilisée pour afficher le résultat
#print("La chaîne inversée est :", chaine_inversee)
#################################################################################################

#################################################################################################
        # Demande à l'utilisateur d'entrer une chaîne de caractères
        # La fonction input() récupère la saisie de l'utilisateur et la stocke dans la variable 'chaine'
#chaine = input("Entrez une chaîne de caractères : ")

        # Initialise une chaîne vide pour stocker le résultat inversé
#chaine_inversee = ""

        # Initialise un compteur pour calculer la longueur de la chaîne
#longueur = 0

        # Boucle for qui parcourt chaque caractère de la chaîne pour compter sa longueur
#for caractere in chaine:
    #longueur += 1  # Incrémente le compteur pour chaque caractère

        # Initialise l'index à la dernière position de la chaîne
        # On utilise longueur - 1 car les indices commencent à 0
#index = longueur - 1

        # Boucle while qui s'exécute tant que l'index est supérieur ou égal à 0
#while index >= 0:
        # Ajoute le caractère à la position 'index' de 'chaine' à la fin de 'chaine_inversee'
    #chaine_inversee += chaine[index]
        # Décrémente l'index pour passer au caractère précédent
    #index -= 1

        # Affiche la chaîne inversée
        # La fonction print() est utilisée pour afficher le résultat
#print("La chaîne inversée est :", chaine_inversee)
#################################################################################################


#################################################################################################
        # Demande à l'utilisateur d'entrer une chaîne de caractères
        # La fonction input() récupère la saisie de l'utilisateur et la stocke dans la variable 'chaine'
chaine = input("Entrez une chaîne de caractères : ")

        # Affiche la chaîne inversée directement dans le print
        # chaine[::-1] est une technique de découpage (slicing) qui inverse la chaîne :
        #   - Le premier ':' indique le début de la chaîne (par défaut, c'est le début)
        #   - Le deuxième ':' indique la fin de la chaîne (par défaut, c'est la fin)
        #   - '-1' est le pas, qui indique qu'on parcourt la chaîne de la fin vers le début
print(chaine[::-1])
#################################################################################################
