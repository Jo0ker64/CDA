import json  # Importation du module JSON pour lire et écrire les contacts dans un fichier JSON

class ContactManager:
    """
    Classe pour gérer un carnet de contacts avec des fonctionnalités d'ajout, de modification, de suppression et de recherche.
    """

    def __init__(self, filename="contacts.json"):
        """
        Initialise le gestionnaire de contacts.

        :param filename: Nom du fichier JSON pour stocker les contacts
        """
        # Nom du fichier de sauvegarde des contacts
        self.filename = filename
        # Chargement initial des contacts à partir du fichier
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """
        Charge les contacts depuis le fichier JSON.

        :return: Dictionnaire des contacts ou un dictionnaire vide si le fichier n'existe pas
        """
        try:
            # Ouvre le fichier en mode lecture
            with open(self.filename, "r") as file:
                # Charge et retourne les contacts en tant que dictionnaire
                return json.load(file)
        except FileNotFoundError:
            # Si le fichier n'existe pas, retourne un dictionnaire vide
            return {}

    def save_contacts(self):
        """
        Sauvegarde les contacts dans le fichier JSON.
        """
        # Ouvre le fichier en mode écriture
        with open(self.filename, "w") as file:
            # Enregistre les contacts avec une indentation pour une meilleure lisibilité
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        """
        Ajoute un nouveau contact en demandant les informations à l'utilisateur.
        """
        # Demande les informations de contact à l'utilisateur
        first_name = input("Prénom : ")
        last_name = input("Nom : ")
        phone = input("Numéro de téléphone : ")
        email = input("Adresse email : ")
        address = input("Adresse : ")
        
        # Crée le nom complet en combinant le prénom et le nom
        full_name = f"{first_name} {last_name}"
        # Vérifie si le contact existe déjà
        if full_name in self.contacts:
            print("Ce contact existe déjà.")
            return
        
        # Ajoute le contact au dictionnaire des contacts
        self.contacts[full_name] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "address": address
        }
        # Sauvegarde les contacts dans le fichier
        self.save_contacts()
        print(f"Contact {full_name} ajouté avec succès.")

    def update_contact(self):
        """
        Met à jour les informations d'un contact existant.
        """
        # Demande le nom complet du contact à modifier
        full_name = input("Nom complet du contact à modifier : ")
        # Vérifie si le contact existe
        if full_name not in self.contacts:
            print("Contact introuvable.")
            return
        
        # Affiche les valeurs actuelles et permet de les modifier
        print("Laissez vide si vous ne voulez pas modifier l'information.")
        first_name = input(f"Nouveau prénom ({self.contacts[full_name]['first_name']}) : ") or self.contacts[full_name]['first_name']
        last_name = input(f"Nouveau nom ({self.contacts[full_name]['last_name']}) : ") or self.contacts[full_name]['last_name']
        phone = input(f"Nouveau numéro de téléphone ({self.contacts[full_name]['phone']}) : ") or self.contacts[full_name]['phone']
        email = input(f"Nouvelle adresse email ({self.contacts[full_name]['email']}) : ") or self.contacts[full_name]['email']
        address = input(f"Nouvelle adresse ({self.contacts[full_name]['address']}) : ") or self.contacts[full_name]['address']
        
        # Crée le nouveau nom complet
        new_full_name = f"{first_name} {last_name}"
        # Si le nom complet a changé, supprime l'ancien contact
        if new_full_name != full_name:
            del self.contacts[full_name]
        
        # Met à jour le contact avec les nouvelles informations
        self.contacts[new_full_name] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "address": address
        }
        # Sauvegarde les modifications
        self.save_contacts()
        print(f"Contact {new_full_name} mis à jour avec succès.")

    def delete_contact(self):
        """
        Supprime un contact existant.
        """
        # Demande le nom complet du contact à supprimer
        full_name = input("Nom complet du contact à supprimer : ")
        # Vérifie si le contact existe
        if full_name in self.contacts:
            # Supprime le contact
            del self.contacts[full_name]
            # Sauvegarde les modifications
            self.save_contacts()
            print(f"Contact {full_name} supprimé avec succès.")
        else:
            print("Contact introuvable.")

    def search_contact(self):
        """
        Recherche et affiche les informations d'un contact.
        """
        # Demande le nom complet du contact à rechercher
        full_name = input("Nom complet du contact à rechercher : ")
        # Récupère les informations du contact s'il existe
        contact = self.contacts.get(full_name)
        if contact:
            # Affiche les informations du contact
            print(f"Nom: {full_name}")
            print(f"Prénom: {contact['first_name']}")
            print(f"Nom: {contact['last_name']}")
            print(f"Téléphone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Adresse: {contact['address']}")
        else:
            print("Contact introuvable.")

    def list_contacts(self):
        """
        Affiche la liste de tous les contacts.
        """
        # Vérifie si la liste des contacts est vide
        if not self.contacts:
            print("Aucun contact trouvé.")
            return
        # Parcourt et affiche chaque contact
        for full_name, info in self.contacts.items():
            print(f"Nom: {full_name}, Téléphone: {info['phone']}, Email: {info['email']}")

def contact():
    """
    Fonction principale qui gère l'interface utilisateur pour le gestionnaire de contacts.
    """
    # Crée une instance de ContactManager
    manager = ContactManager()
    # Boucle principale pour le menu
    while True:
        # Affiche le menu des options
        print("\n1. Ajouter un contact")
        print("2. Modifier un contact")
        print("3. Supprimer un contact")
        print("4. Rechercher un contact")
        print("5. Lister tous les contacts")
        print("6. Quitter")
        
        # Récupère le choix de l'utilisateur
        choice = input("Choisissez une option (1-6) : ")
        
        # Exécute la fonction en fonction du choix de l'utilisateur
        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.update_contact()
        elif choice == '3':
            manager.delete_contact()
        elif choice == '4':
            manager.search_contact()
        elif choice == '5':
            manager.list_contacts()
        elif choice == '6':
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Point d'entrée du programme
if __name__ == "__main__":
    # Lance l'interface utilisateur pour le gestionnaire de contacts
    contact()
