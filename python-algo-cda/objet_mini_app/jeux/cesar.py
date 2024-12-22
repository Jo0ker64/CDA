class CodeurDecodeurCesar:
    """
    Classe pour coder et décoder des messages en utilisant le chiffrement de César.
    """

    def __init__(self):
        """
        Initialise l'alphabet utilisé pour le chiffrement et le déchiffrement.
        """
        # Alphabet utilisé pour le chiffrement de César
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def coder(self, message, decalage):
        """
        Code un message avec le chiffrement de César en appliquant un décalage.

        :param message: Le message à coder
        :param decalage: Le décalage à appliquer
        :return: Le message codé
        """
        # Initialise une chaîne vide pour le message codé
        message_code = ''

        # Parcourt chaque caractère du message en majuscule
        for caractere in message.upper():
            # Vérifie si le caractère est une lettre de l'alphabet
            if caractere in self.alphabet:
                # Trouve l'index du caractère dans l'alphabet
                index = self.alphabet.index(caractere)
                # Calcule la nouvelle position après application du décalage
                nouvelle_position = (index + decalage) % len(self.alphabet)
                # Ajoute la lettre codée au message codé
                message_code += self.alphabet[nouvelle_position]
            else:
                # Ajoute les caractères non alphabétiques sans modification
                message_code += caractere

        # Retourne le message codé
        return message_code

    def decoder(self, message, decalage):
        """
        Décode un message chiffré en utilisant un décalage négatif.

        :param message: Le message à décoder
        :param decalage: Le décalage appliqué lors du codage
        :return: Le message décodé
        """
        # Utilise la méthode de codage avec le décalage inversé pour décoder
        return self.coder(message, -decalage)

    def lancer(self):
        """
        Lance le programme interactif de codage et de décodage pour l'utilisateur.
        """
        # Affiche un message de bienvenue
        print("Bienvenue dans le codeur/décodeur César!")

        # Boucle principale pour traiter plusieurs messages
        while True:
            # Demande à l'utilisateur s'il veut coder, décoder, ou quitter
            choix = input("Voulez-vous coder (C) ou décoder (D) un message ? (ou 'Q' pour quitter): ").upper()
            
            # Vérifie si l'utilisateur a choisi de quitter
            if choix == 'Q':
                break
            # Vérifie si le choix est valide
            elif choix not in ['C', 'D']:
                print("Choix invalide. Veuillez entrer 'C', 'D' ou 'Q'.")
                continue

            # Demande le message à traiter
            message = input("Entrez le message : ")

            # Demande le décalage et s'assure qu'il s'agit d'un entier
            try:
                decalage = int(input("Entrez le décalage : "))
            except ValueError:
                # Informe l'utilisateur que le décalage doit être un nombre entier
                print("Erreur : Le décalage doit être un nombre entier.")
                continue

            # Applique le codage ou le décodage selon le choix de l'utilisateur
            if choix == 'C':
                # Code le message
                resultat = self.coder(message, decalage)
                # Affiche le message codé
                print(f"Message codé : {resultat}")
            else:
                # Décode le message
                resultat = self.decoder(message, decalage)
                # Affiche le message décodé
                print(f"Message décodé : {resultat}")
            
            # Ajoute une ligne vide pour une meilleure lisibilité entre les messages
            print()

        # Affiche un message de fin
        print("Merci d'avoir utilisé le codeur/décodeur César!")

# Point d'entrée du programme
if __name__ == "__main__":
    # Crée une instance de CodeurDecodeurCesar
    cesar = CodeurDecodeurCesar
