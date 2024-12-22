def fibonacci(n):
    """Génère les n premiers termes de la suite de Fibonacci."""
    # Initialisation de la liste avec les deux premiers termes de la suite
    fib = [0, 1]  
    
    # Boucle jusqu'à ce que la liste contienne n termes
    while len(fib) < n:
        # Ajoute à la liste la somme des deux derniers termes
        fib.append(fib[-1] + fib[-2])  
    
    # Retourne la liste complète
    return fib

# Demande à l'utilisateur le nombre de termes souhaités et convertit l'entrée en entier
n = int(input("Combien de termes de la suite de Fibonacci voulez-vous générer ? "))

# Appelle la fonction fibonacci avec le nombre de termes demandé et stocke le résultat
suite_fib = fibonacci(n)

# Affiche un message indiquant le nombre de termes générés
print(f"Les {n} premiers termes de la suite de Fibonacci sont :")
# Affiche la liste complète des termes
print(suite_fib)

# Boucle à travers la liste des termes avec leur index
for i, terme in enumerate(suite_fib):
    # Affiche chaque terme avec son index dans la suite
    print(f"F({i}) = {terme}")
