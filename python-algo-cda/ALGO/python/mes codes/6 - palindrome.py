# Votre script demande un mot en entrée, indiquez si le mot est un palindrome ou non

# mot = input("Entrez un mot : ")

# mot_traite = mot.lower().replace(" ", "")

# if mot_traite == mot_traite[::-1]:
#     print(f"'{mot}' est un palindrome.")
# else:
#     print(f"'{mot}' n'est pas un palindrome.")


# Demande à l'utilisateur d'entrer un mot et le convertit immédiatement en minuscules
# input() récupère la saisie de l'utilisateur
# lower() convertit toute la chaîne en minuscules pour ignorer la casse lors de la vérification
mot = input("Entrez un mot : ").lower()

# Vérifie si le mot est un palindrome
# mot[::-1] crée une version inversée du mot :
#   - Les deux ':' indiquent qu'on prend toute la chaîne
#   - '-1' est le pas, qui indique qu'on parcourt la chaîne de la fin vers le début
if mot == mot[::-1]:
        # Si le mot est égal à sa version inversée, c'est un palindrome
        print("C'est un palindrome")
else:
        # Si le mot n'est pas égal à sa version inversée, ce n'est pas un palindrome
        print("Ce n'est pas un palindrome")

