# Votre script demande 2 nombres en entrée et vous affichez le résultat de l’addition

# Assigne la valeur 2 à la variable x
# x = 2

# Assigne la valeur 3 à la variable y
# y = 3

# Calcule la somme de x et y et assigne le résultat à la variable z
# z = x + y

# Affiche la valeur de z, qui est la somme de x et y
# print(z)


# Demande à l'utilisateur d'entrer le premier nombre
# La fonction input() récupère une chaîne de caractères
# float() convertit cette chaîne en nombre décimal
num1 = float(input("Entrez le premier nombre : "))

# Demande à l'utilisateur d'entrer le second nombre
# Même processus que pour num1
num2 = float(input("Entrez le second nombre : "))

# Affiche la somme des deux nombres
# f"..." est une f-string, permettant d'insérer des valeurs dans la chaîne
# {num1 + num2} calcule la somme et l'insère dans la chaîne
print(f"La somme est : {num1 + num2}")

