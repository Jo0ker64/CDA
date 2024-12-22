# Demande à l'utilisateur le nombre de termes à générer et convertit l'entrée en entier
n = int(input("Combien de termes de la suite de Fibonacci voulez-vous générer ? "))

# Initialisation des deux premiers termes de la suite de Fibonacci
a, b = 0, 1

# Création d'une liste vide pour stocker les termes de la suite de Fibonacci
fibonacci = []

# Boucle pour générer la suite de Fibonacci
for i in range(n):
    # Ajoute le terme actuel (a) à la liste
    fibonacci.append(a)
    # Met à jour les valeurs de a et b pour la prochaine itération
    # a devient b, et b devient la somme de a et b
    a, b = b, a + b

# Affichage d'un message indiquant le nombre de termes générés
print(f"Les {n} premiers termes de la suite de Fibonacci sont :")
# Affichage de la liste complète des termes de Fibonacci
print(fibonacci)

# Affichage d'un en-tête pour le détail de la suite
print("\nDétail de la suite :")
# Boucle pour afficher chaque terme avec son index
for i, terme in enumerate(fibonacci):
    # Affiche le numéro du terme (i) et sa valeur
    print(f"F({i}) = {terme}")
