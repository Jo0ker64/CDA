# utilisation du mot clé class pour créer mon objet (ici Personnage)
class Personnage:
    #Attributs (caractèristiques qui vont definir mon objet (mon personnage))
    pseudo = "Jean"
    force = 80
    point_de_vie = 100
    
    # __init__ sert de constructeur a l'objet (permet de définir les valeurs attribuer a l'objet ciblé)
    # en python les methodes d'un objet doit recevoir self en paramètres pour pouvoir acceder au attribut ou aux méthodes de l'objet
    def __init__(self, pseudo, force):
        self.pseudo = pseudo
        self.force = force

    #Methodes (Actions possible par l'objet)

    # Présentation breve du personnage avec les infos sur le pseudos, la force et les points de vie
    def SePresenter(self):
        # Je suis Jean, j'ai 80 en force et j'ai 100 points de vie
        # ATTENTION le mot clé self est la pour faire référence a l'objet lui meme (l'id de l'objet et pas l'objet de base)
        # Utilisation du mot clé self pour faire référence a l'objet lui meme (personnage1, personnage2, personnage3)
        return print("Je suis " + self.pseudo + ", j'ai " + str(self.force) + " en force et j'ai " + str(self.point_de_vie) + " points de vie")

# Création/Instanciation du premier personnage a partir de la Class : Personnage
personnage1 = Personnage("Jean-Michel", 800)
# Création/Instanciation du second personnage a partir de la class : Personnage
personnage2 = Personnage("Perso2", 40)
# Création/Instanciation du troisième personnage a partir de la class : Personnage
personnage3 = Personnage("Koukou", 99999999999)

# Affiche le pseudo du perso1 et perso2
# On utilise le "." pour indiquer a l'objet que l'on souhaite acceder a son attribue pseudo
print("Pseudo perso1 : " + personnage1.pseudo)
print("Pseudo perso2 : " + personnage2.pseudo)
# Affiche les pdv du perso1 et perso2
print("PdV perso1 : " + str(personnage1.point_de_vie))
print("PdV perso2 : " + str(personnage2.point_de_vie))
# Affiche la force du perso1 et perso2
print("Force perso2 : " + str(personnage2.force))
print("Force perso1 : " + str(personnage1.force))


# Affiche la présentation du perso1, 2 et 3
# On utilise ici le "." pour indiquer a l'objet que l'on souhaite acceder a sa méthode "SePresenter"
personnage1.SePresenter()
personnage2.SePresenter()
personnage3.SePresenter()