# Votre script prend le numéro d’une table en entrée, affichez la table complète jusqu’à 10.


# try:
#     # Demande à l'utilisateur d'entrer un nombre et le convertit en entier
#     numero_table = int(input("Entrez le numéro de la table de multiplication que vous souhaitez afficher : "))
# except ValueError:
#     # Gère l'erreur si l'utilisateur n'entre pas un nombre valide
#     print("Veuillez entrer un nombre entier valide.")
#     exit()  # Quitte le programme

# # Affiche l'en-tête de la table
# print(f"\nTable de multiplication de {numero_table} :")
# print("-" * 30)  # Affiche une ligne de séparation

# # Boucle pour générer la table de multiplication
# for i in range(1, 11):
#     resultat = numero_table * i
#     # Affiche chaque ligne de la table, formatée pour l'alignement
#     print(f"{numero_table} x {i:2} = {resultat:3}")

# # Affiche une ligne de séparation à la fin
# print("-" * 30)

#########################################################################################################################

# Boucle externe pour les multiplicandes de 1 à 10
for a in range(1, 11):
    # Boucle interne pour les multiplicateurs de 1 à 10
    for b in range(1, 11):
        # Affiche chaque multiplication
        print(a, '×', b, '=', a * b)
    # Affiche une ligne de séparation après chaque table
    print('---')
