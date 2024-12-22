# Votre script prend une liste en entrée, indiquez le plus petit élément de la liste

liste = [10, 50, 130, 2597,1,12,17,64]
resultat = liste[0]

for nb in liste:
    #print(nb)
    if (nb < resultat):
        resultat = nb

print(resultat)