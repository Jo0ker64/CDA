liste = [12, 84, 34, 87, 12, 38, 84, 84]
valeurs_uniques_dans_liste = []

for valeur in liste:
    if (valeur not in valeurs_uniques_dans_liste):
        valeurs_uniques_dans_liste.append(valeur)

print(valeurs_uniques_dans_liste)
