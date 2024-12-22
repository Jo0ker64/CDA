# fichier : fonction_jeux/morse.py

# Dictionnaire pour la conversion en Code Morse
morse = {
    ' ': ' ',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

# Dictionnaire inverse pour le décodage du Code Morse
morse_inv = {valeur: cle for cle, valeur in morse.items()}

def coder_morse(message):
    """
    Cette fonction code un message en Code Morse.
    Elle prend en entrée le message et retourne le message codé en Morse.
    """
    code = []
    message = message.upper()  # Convertit le message en majuscules
    for caractere in message:
        if caractere in morse:
            code.append(morse[caractere])
        else:
            # Ajoute un espace pour les caractères non reconnus
            code.append(' ')
    return " ".join(code)  # Retourne le code Morse avec des espaces entre les caractères

def decoder_morse(code_morse):
    """
    Cette fonction décode un message en Code Morse.
    Elle prend en entrée le code Morse et retourne le message en lettres normales.
    """
    phrase = []
    mots = code_morse.split("   ")  # Sépare les mots par trois espaces (convention pour les mots en Morse)
    for mot in mots:
        lettres = mot.split()  # Sépare chaque lettre par un espace
        for lettre in lettres:
            if lettre in morse_inv:
                phrase.append(morse_inv[lettre])
        phrase.append(" ")  # Ajoute un espace pour séparer les mots
    return "".join(phrase).strip()  # Retourne la phrase déchiffrée

def code_morse():
    """
    Fonction principale pour l'interaction avec l'utilisateur en Code Morse.
    """
    print("Bienvenue dans le codeur/décodeur Morse!")
    
    while True:
        # Demande à l'utilisateur s'il veut coder ou décoder
        choix = input("Voulez-vous coder (C) ou décoder (D) un message ? (ou 'Q' pour quitter): ").upper()
        if choix == 'Q':
            break
        elif choix not in ['C', 'D']:
            print("Choix invalide. Veuillez entrer 'C', 'D' ou 'Q'.")
            continue

        # Demande le message ou le code Morse à traiter
        if choix == 'C':
            message = input("Entrez le message à coder : ")
            resultat = coder_morse(message)
            print(f"Message codé en Morse : {resultat}")
        else:  # choix == 'D'
            code = input("Entrez le code Morse à décoder (séparez les lettres par un espace, les mots par trois espaces) : ")
            resultat = decoder_morse(code)
            print(f"Message décodé : {resultat}")
        
        print()

    print("Merci d'avoir utilisé le codeur/décodeur Morse!")

# Point d'entrée du programme
if __name__ == "__main__":
    code_morse()
