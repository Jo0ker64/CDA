# Votre script demande 1 nombre en entrée et vous retournez “pair” ou “impair”

# Demande à l'utilisateur d'entrer un nombre
# input() récupère la saisie de l'utilisateur sous forme de chaîne
# int() convertit cette chaîne en un entier int = integer
nombre = int(input("entrez un nombre : "))

# Vérifie si le nombre est pair
# L'opérateur % calcule le reste de la division par 2
# Si ce reste est 0, le nombre est pair
if nombre % 2 == 0 :
    # Si la condition est vraie (le nombre est pair), affiche "pair"
    print("Pair !")
else :
    # Si la condition est fausse (le nombre est impair), affiche "impair"
    print("Impair !")


#nb = input("votre nb:")
# if (nb%2 ==0):
#     print("pair")
#elif (nb%2 != 0):
#    print("impair")
#else:
#    print("valeur non connue")