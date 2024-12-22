# Etape 1 :
# 2 nombres via l'user
nb1 = int(input('saisir un nb : '))
nb2 = int(input("saisie un second nb : "))
print(nb1, nb2)

# Etape 2 :
# Affichage du resultat 
# (methode 1)
# on affiche le résultat de l'opération convertie en string
print("Resultat : " + str(nb1+nb2))

# (methode 2)
# on stock le resultat dans une variable de type string
resultat = str(nb1+nb2)
# on affiche la variable
print("Resultat : " + resultat)