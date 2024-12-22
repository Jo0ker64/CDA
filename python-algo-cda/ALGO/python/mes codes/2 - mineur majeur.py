# Votre script demande l’âge d’un utilisateur et vous affichez “majeur” ou “mineur”

# Demande à l'utilisateur d'entrer son âge
# La fonction input() récupère la saisie de l'utilisateur sous forme de chaîne
# int() convertit cette chaîne en un entier

age = int(input("Entrez votre âge : "))

# Vérifie si l'âge est supérieur ou égal à 18
if age >= 18:
        # Si la condition est vraie, affiche "Majeur"
        print("Majeur")
else:
        # Si la condition est fausse (c'est-à-dire que l'âge est inférieur à 18), affiche "Mineur"
        print("Mineur")
