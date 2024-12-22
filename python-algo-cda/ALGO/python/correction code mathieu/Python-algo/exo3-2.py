# Votre script prend une liste de nombres en entrée, indiquez le nombre qui se répète le plus
# de fois dans la liste

nombres = [25, 18, 24, 18, 18, 32, 15, 18, 40]
nombre_unique_dans_liste = []
resultat = 0 
nb_repetition = 0 # = 1 pour le premier tour (1 fois 25) | = 4 pour (4x18)
nb_repetition_hold = 0
for nombre in nombres:
    #print(nombre)
    if (nombre not in nombre_unique_dans_liste):
        nombre_unique_dans_liste.append(nombre)

print(nombre_unique_dans_liste)

# 2 boucles 
# 1 pour parcourir le premier tableau (nombres|nombre_unique_dans_listes)
# 2 boucle pour parcourir le second tableau et faire un compte de la valeur

for valeur in nombre_unique_dans_liste:
    print("Valeur dans nombre unique : " + str(valeur))
    #nb_repetition = 0
    for nb in nombres:
        print("Valeur dans la liste de base : " + str(nb))
        # TEST avant d'avoir le nb de répétitions ?
        if (valeur == nb):
            nb_repetition = nb_repetition + 1
    # ICI
    if (nb_repetition_hold < nb_repetition):
        nb_repetition = nb_repetition_hold
    #nb_repetition_hold = nb_repetition
    print(nb_repetition)
    # JUSTE AVANT LE TOUR D'APRES
    nb_repetition = 0

    print(nb_repetition_hold)
    
    #break
