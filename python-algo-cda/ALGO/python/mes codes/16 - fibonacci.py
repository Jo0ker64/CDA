# Initialisation des variables a et b
a, b = 0, 1

# Boucle while qui continue tant que a est inférieur à 120
while a < 120:
    # Affiche la valeur actuelle de a
    print(a)
    
    # Met à jour les valeurs de a et b pour la prochaine itération
    # a prend la valeur actuelle de b
    # b prend la somme des valeurs actuelles de a et b
    a, b = b, a+b
