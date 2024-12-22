print("Lancement du Gestionnaire de contact ...")

import json

class ContactManager:
    def __init__(self, filename="contacts.json"):
        """
        Initialise le gestionnaire de contacts.
        :param filename: Nom du fichier JSON pour stocker les contacts
        """
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """
        Charge les contacts depuis le fichier JSON.
        :return: Dictionnaire des contacts ou un dictionnaire vide si le fichier n'existe pas
        """
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_contacts(self):
        """
        Sauvegarde les contacts dans le fichier JSON.
        """
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        """
        Ajoute un nouveau contact en demandant les informations à l'utilisateur.
        """
        first_name = input("Prénom : ")
        last_name = input("Nom : ")
        phone = input("Numéro de téléphone : ")
        email = input("Adresse email : ")
        address = input("Adresse : ")
        
        full_name = f"{first_name} {last_name}"
        if full_name in self.contacts:
            print("Ce contact existe déjà.")
            return
        
        self.contacts[full_name] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.save_contacts()
        print(f"Contact {full_name} ajouté avec succès.")

    def update_contact(self):
        """
        Met à jour les informations d'un contact existant.
        """
        full_name = input("Nom complet du contact à modifier : ")
        if full_name not in self.contacts:
            print("Contact introuvable.")
            return
        
        print("Laissez vide si vous ne voulez pas modifier l'information.")
        first_name = input(f"Nouveau prénom ({self.contacts[full_name]['first_name']}) : ") or self.contacts[full_name]['first_name']
        last_name = input(f"Nouveau nom ({self.contacts[full_name]['last_name']}) : ") or self.contacts[full_name]['last_name']
        phone = input(f"Nouveau numéro de téléphone ({self.contacts[full_name]['phone']}) : ") or self.contacts[full_name]['phone']
        email = input(f"Nouvelle adresse email ({self.contacts[full_name]['email']}) : ") or self.contacts[full_name]['email']
        address = input(f"Nouvelle adresse ({self.contacts[full_name]['address']}) : ") or self.contacts[full_name]['address']
        
        new_full_name = f"{first_name} {last_name}"
        if new_full_name != full_name:
            del self.contacts[full_name]
        
        self.contacts[new_full_name] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.save_contacts()
        print(f"Contact {new_full_name} mis à jour avec succès.")

    def delete_contact(self):
        """
        Supprime un contact existant.
        """
        full_name = input("Nom complet du contact à supprimer : ")
        if full_name in self.contacts:
            del self.contacts[full_name]
            self.save_contacts()
            print(f"Contact {full_name} supprimé avec succès.")
        else:
            print("Contact introuvable.")

    def search_contact(self):
        """
        Recherche et affiche les informations d'un contact.
        """
        full_name = input("Nom complet du contact à rechercher : ")
        contact = self.contacts.get(full_name)
        if contact:
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
        if not self.contacts:
            print("Aucun contact trouvé.")
            return
        for full_name, info in self.contacts.items():
            print(f"Nom: {full_name}, Téléphone: {info['phone']}, Email: {info['email']}")

def contact():
    """
    Fonction principale qui gère l'interface utilisateur et les interactions.
    """
    manager = ContactManager()
    while True:
        # Affichage du menu principal
        print("\n1. Ajouter un contact")
        print("2. Modifier un contact")
        print("3. Supprimer un contact")
        print("4. Rechercher un contact")
        print("5. Lister tous les contacts")
        print("6. Quitter")
        
        choice = input("Choisissez une option (1-6) : ")
        
        # Traitement du choix de l'utilisateur
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

if __name__ == "__main__":
    contact()
