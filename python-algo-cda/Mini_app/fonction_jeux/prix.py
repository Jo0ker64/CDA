print("Lancement du juste prix ...")
import random

def juste_prix():
    # Définir les limites du jeu
    limite_basse = 1
    limite_haute = 50
    
    # L'ordinateur choisit un nombre aléatoire
    prix = random.randint(limite_basse, limite_haute)
    
    # Nombre maximum d'essais
    max_essais = 5
    
    print(f"Bienvenue au Juste Prix !")
    print(f"Je pense à un nombre entre {limite_basse} et {limite_haute}.")
    print(f"Vous avez {max_essais} essais pour le deviner.")
    
    for essai in range(1, max_essais + 1):
        # Demander au joueur de deviner
        try:
            guess = int(input(f"Essai {essai}/{max_essais} - Devinez le prix : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        
        # Vérifier la proposition du joueur
        if guess < prix:
            print("C'est plus !")
        elif guess > prix:
            print("C'est moins !")
        else:
            print(f"Bravo ! Vous avez trouvé le juste prix en {essai} essai(s).")
            return
        
        # Informer le joueur du nombre d'essais restants
        if essai < max_essais:
            print(f"Il vous reste {max_essais - essai} essai(s).")
    
    # Si le joueur n'a pas trouvé après 4 essais
    print(f"Désolé, vous n'avez pas trouvé le juste prix en {max_essais} essais.")
    print(f"Le juste prix était {prix}.")

# Lancer le jeu
if __name__ == "__main__":
    juste_prix()

