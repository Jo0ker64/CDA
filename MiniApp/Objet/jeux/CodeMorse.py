class MorseCode:
    """
    Classe pour coder et décoder des messages en Code Morse.
    """
    def __init__(self):
        """
        Initialise les dictionnaires pour le codage et le décodage en Morse.
        """
        self.morse = {
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
        self.morse_inv = {valeur: cle for cle, valeur in self.morse.items()}  # Inverse du dictionnaire pour décoder

    def coder(self, message):
        """
        Code un message en Morse.
        :param message: str, le message à coder.
        :return: str, le message codé en Morse.
        """
        code = []
        message = message.upper()  # Convertit en majuscules
        for caractere in message:
            if caractere in self.morse:
                code.append(self.morse[caractere])
            else:
                code.append(' ')  # Caractères non reconnus
        return " ".join(code)

    def decoder(self, code_morse):
        """
        Décode un message en Morse.
        :param code_morse: str, le code Morse à décoder.
        :return: str, le message décodé.
        """
        phrase = []
        mots = code_morse.split("   ")  # Séparation des mots par trois espaces
        for mot in mots:
            lettres = mot.split()  # Séparation des lettres par un espace
            for lettre in lettres:
                if lettre in self.morse_inv:
                    phrase.append(self.morse_inv[lettre])
            phrase.append(" ")  # Espace pour séparer les mots
        return "".join(phrase).strip()

    def interaction(self):
        """
        Fournit une interface interactive pour coder ou décoder des messages.
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

            # Traite le choix
            if choix == 'C':
                message = input("Entrez le message à coder : ")
                resultat = self.coder(message)
                print(f"Message codé en Morse : {resultat}")
            else:  # choix == 'D'
                code = input("Entrez le code Morse à décoder (séparez les lettres par un espace, les mots par trois espaces) : ")
                resultat = self.decoder(code)
                print(f"Message décodé : {resultat}")
            
            print()

        print("Merci d'avoir utilisé le codeur/décodeur Morse!")


# Exemple d'utilisation autonome
if __name__ == "__main__":
    morse = MorseCode()  # Crée une instance de la classe
    morse.interaction()  # Lance l
