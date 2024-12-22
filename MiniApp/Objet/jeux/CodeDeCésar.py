class CodeurDecodeurCesar:
    """
    Classe pour coder et décoder des messages avec le chiffrement de César.
    """

    def __init__(self):
        """
        Initialise l'alphabet utilisé pour le chiffrement.
        """
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def coder(self, message, decalage):
        """
        Code un message en utilisant le chiffrement de César.

        :param message: str, le message à coder.
        :param decalage: int, le décalage à appliquer.
        :return: str, le message codé.
        """
        message_code = ''
        # Parcourt chaque caractère du message
        for caractere in message.upper():
            if caractere in self.alphabet:
                index = self.alphabet.index(caractere)
                nouvelle_position = (index + decalage) % 26
                message_code += self.alphabet[nouvelle_position]
            else:
                message_code += caractere  # Conserve les caractères non alphabétiques
        return message_code

    def decoder(self, message, decalage):
        """
        Décode un message chiffré en utilisant le chiffrement de César.

        :param message: str, le message à décoder.
        :param decalage: int, le décalage appliqué lors du codage.
        :return: str, le message décodé.
        """
        return self.coder(message, -decalage)

    def lancer(self):
        """
        Méthode principale pour lancer le programme interactif.
        """
        print("Bienvenue dans le codeur/décodeur César!")

        while True:
            # Demande à l'utilisateur s'il veut coder ou décoder un message
            choix = input("Voulez-vous coder (C) ou décoder (D) un message ? (ou 'Q' pour quitter): ").upper()
            if choix == 'Q':
                break
            elif choix not in ['C', 'D']:
                print("Choix invalide. Veuillez entrer 'C', 'D' ou 'Q'.")
                continue

            # Demande le message à traiter
            message = input("Entrez le message : ")

            # Demande le décalage avec gestion des erreurs
            try:
                decalage = int(input("Entrez le décalage : "))
            except ValueError:
                print("Erreur : Le décalage doit être un nombre entier.")
                continue

            # Effectue le codage ou le décodage
            if choix == 'C':
                resultat = self.coder(message, decalage)
                print(f"Message codé : {resultat}")
            else:  # choix == 'D'
                resultat = self.decoder(message, decalage)
                print(f"Message décodé : {resultat}")

            print()  # Ajoute une ligne vide pour la lisibilité

        print("Merci d'avoir utilisé le codeur/décodeur César!")


# Exemple d'utilisation autonome
if __name__ == "__main__":
    cesar = CodeurDecodeurCesar()  # Crée une instance de la classe
    cesar.lancer()  # Lance le programme interactif
