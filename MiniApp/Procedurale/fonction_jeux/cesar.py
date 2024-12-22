# Affiche un message indiquant le lancement du programme
print("Lancement du Codeur/Décodeur César ...")

def coder_cesar(message, decalage):
    """
    Cette fonction code un message avec le chiffrement de César.
    Elle prend en entrée le message et le décalage, et retourne le message codé.
    """
    # Définit l'alphabet utilisé pour le chiffrement
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Initialise une chaîne vide pour stocker le message codé
    message_code = ''

    # Parcourt chaque caractère du message
    for caractere in message.upper():
        # Vérifie si le caractère est une lettre de l'alphabet
        if caractere in alphabet:
            # Trouve l'index de la lettre dans l'alphabet
            index = alphabet.index(caractere)
            # Calcule la nouvelle position après le décalage
            nouvelle_position = (index + decalage) % 26
            # Ajoute la lettre codée au message
            message_code += alphabet[nouvelle_position]
        else:
            # Conserve les caractères non alphabétiques tels quels
            message_code += caractere

    # Retourne le message codé
    return message_code

def decoder_cesar(message, decalage):
    """
    Cette fonction décode un message chiffré avec César.
    Elle utilise la fonction de codage avec un décalage négatif.
    """
    # Utilise la fonction de codage avec un décalage négatif pour décoder
    return coder_cesar(message, -decalage)

def cesar():
    # Affiche un message de bienvenue
    print("Bienvenue dans le codeur/décodeur César!")
    
    # Boucle principale du programme
    while True:
        # Demande à l'utilisateur s'il veut coder ou décoder
        choix = input("Voulez-vous coder (C) ou décoder (D) un message ? (ou 'Q' pour quitter): ").upper()
        # Vérifie si l'utilisateur veut quitter
        if choix == 'Q':
            break
        # Vérifie si le choix est valide
        elif choix not in ['C', 'D']:
            print("Choix invalide. Veuillez entrer 'C', 'D' ou 'Q'.")
            continue

        # Demande le message à traiter
        message = input("Entrez le message : ")

        # Demande le décalage et vérifie qu'il s'agit bien d'un nombre
        try:
            decalage = int(input("Entrez le décalage : "))
        except ValueError:
            print("Erreur : Le décalage doit être un nombre entier.")
            continue

        # Applique le codage ou le décodage selon le choix
        if choix == 'C':
            # Code le message
            resultat = coder_cesar(message, decalage)
            # Affiche le message codé
            print(f"Message codé : {resultat}")
        else:  # choix == 'D'
            # Décode le message
            resultat = decoder_cesar(message, decalage)
            # Affiche le message décodé
            print(f"Message décodé : {resultat}")
        
        # Ajoute une ligne vide pour la lisibilité
        print()

    # Affiche un message de fin
    print("Merci d'avoir utilisé le codeur/décodeur César!")

# Vérifie si le script est exécuté directement (et non importé)
if __name__ == "__main__":
    # Appelle la fonction principale
    cesar()
