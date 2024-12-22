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
        except (FileNotFoundError, json.JSONDecodeError):
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
        first_name = input("Prénom : ").strip()
        last_name = input("Nom : ").strip()
        phone = input("Numéro de téléphone : ").strip()
        email = input("Adresse email : ").strip()
        address = input("Adresse : ").strip()

        if not first_name or not last_name:
            print("Erreur : Le prénom et le nom sont obligatoires.")
            return

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
        full_name = input("Nom complet du contact à modifier : ").strip()
        if full_name not in self.contacts:
            print("Contact introuvable.")
            return

        print("Laissez vide si vous ne voulez pas modifier l'information.")
        contact = self.contacts[full_name]
        first_name = input(f"Nouveau prénom ({contact['first_name']}) : ").strip() or contact['first_name']
        last_name = input(f"Nouveau nom ({contact['last_name']}) : ").strip() or contact['last_name']
        phone = input(f"Nouveau numéro de téléphone ({contact['phone']}) : ").strip() or contact['phone']
        email = input(f"Nouvelle adresse email ({contact['email']}) : ").strip() or contact['email']
        address = input(f"Nouvelle adresse ({contact['address']}) : ").strip() or contact['address']

        new_full_name = f"{first_name} {last_name}"
        if new_full_name != full_name:
            self.contacts.pop(full_name)

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
        full_name = input("Nom complet du contact à supprimer : ").strip()
        if full_name in self.contacts:
            confirm = input(f"Êtes-vous sûr de vouloir supprimer {full_name} ? (O/N) : ").strip().lower()
            if confirm == 'o':
                del self.contacts[full_name]
                self.save_contacts()
                print(f"Contact {full_name} supprimé avec succès.")
        else:
            print("Contact introuvable.")

    def search_contact(self):
        """
        Recherche et affiche les informations d'un contact.
        """
        full_name = input("Nom complet du contact à rechercher : ").strip()
        contact = self.contacts.get(full_name)
        if contact:
            print(f"\nNom : {full_name}")
            for key, value in contact.items():
                print(f"{key.capitalize()} : {value}")
        else:
            print("Contact introuvable.")

    def list_contacts(self):
        """
        Affiche la liste de tous les contacts.
        """
        if not self.contacts:
            print("Aucun contact trouvé.")
            return
        print("\nListe des contacts :")
        for full_name, info in self.contacts.items():
            print(f"Nom : {full_name}, Téléphone : {info['phone']}, Email : {info['email']}")


def contact():
    """
    Fonction principale qui gère l'interface utilisateur et les interactions.
    """
    manager = ContactManager()
    while True:
        print("\n1. Ajouter un contact")
        print("2. Modifier un contact")
        print("3. Supprimer un contact")
        print("4. Rechercher un contact")
        print("5. Lister tous les contacts")
        print("6. Quitter")

        choice = input("Choisissez une option (1-6) : ").strip()
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
