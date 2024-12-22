****************************Dictionnaire****************************

# Créer une dictionnaire (vide)
product = {}

# Créer une dictionnaire avec clé et valeur
product = {'id': 100, 'name': 'iPadPro'}

# Accès au dictionnaire par une clé
print(product['name']) # iPadPro

# Accès au dictionnaire avec fonction 'get'
product.get('name') # Si clé existe pas alors retourne 'None'
product.get('name', 'default value') # Si clé existe pas alors retourne une valeur par défaut

# Adding a new key/value
product['description'] = "Modern mobile device"

# Obtenir une liste des clés d'un dictionnaire
product.keys() # ['id', 'name', 'description']

# Obtenir une liste des valeurs d'un dictionnaire
product.values() # ['100', 'iPadPro', 'Modern mobile device']

# Créer une liste de dictionnaire
products = [
    {'id': 100, 'name': 'iPadPro'},
    {'id': 200, 'name': 'iPhone 12'},
    {'id': 300, 'name': 'Charger'},
]

# Accès à une liste de dictionnaire
print(products[2]['name']) # Charger

# Recherche dans une liste de dictionnaire
items_match = [item for product in products if product['id'] == 300]
# [{'id': 300, 'name': 'Charger'}]

# Somme dans une liste de dictionnaire
total = sum([product['price'] for product in products])



*****************************Fonctions*****************************

# Créer une fonction
def say_hello():
    print('Hello World')

# Fonction avec arguments (et valeur par défaut)
def say_hello(name = 'no name'):
    print(f"Hello {name}") 

# Fonction avec arguments (et valeur optionnel)
def say_hello(name = None):
    if name:
        print(f"Hello {name}") 
    else:
        print('Hello World')

# Appel d'une fonction
say_hello('Mike') # Hello Mike

# Appel d'une fonction avec un argument nommé
say_hello(name = 'Mike') 

# Fonction retournant une valeur
def add(num1, num2):
   return num1 + num2

num = add(10, 20) # 30

# Fonction avec un nombres indéterminé d'arguments (*args)
def say_hello(*names):
    for name in names:
        print(f"Hello {name}")

# Fonction avec un nombres indéterminé d'arguments de type keyword (**kwargs)
def say_hello(**kwargs):
    print(kwargs['name'])
    print(kwargs['age'])

say_hello(name = 'Mike', age = 45)

# Fonction Lambda (syntax abbrégé)
x = lambda num : num + 10
print(x(20)) # 30


******************************Date et heure******************************

from datetime import datetime, timedelta

# Retourne la date et l'heure courante
datetime.now()

# Créer un object date et time courant
date = datetime(2020,12,31) # Dec 31 2020

# Addition de date et d'heure (weeks, days, hours, minutes, seconds) 
new_year = date + timedelta(days=1) # Jan 1 2021

# Convertir une date en chaîne de caractère
new_year.strftime('%Y/%m/%d %H %M %S') # 2021/01/01 00 00 00 
new_year.strftime('%A, %b %d') # Friday, Jan 01

# Extraire l'année et le mois d'une date
year = new_year.year # 2021
month = new_year.month # 01


***************************Gestion des fichiers***************************

# Lecture d'un fichier
filename = 'demo.txt'
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line)

# Écriture d'un fichier
filename = 'settings.txt'
with open(filename, 'w') as file:
    file.write("MAX_USER = 100")

# Est-ce que le fichier existe?
from os import path
path.exists('templates/index.html') # True/False

# Exportation en CSV
import csv
csv_file = 'export.csv'
csv_columns = products[0].keys() # ['id', 'name']
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for item in products:
        writer.writerow(item)


*********************************Gestion des exceptions et erreurs*********************************

age_string = input('Your age? ')

try:
    age = int(age_string)
except ValueError:
    print("Please enter a numeric value")
else:
    print("Your age is saved!")


******************************************Programmation orienté objet******************************************

# Créer une classe
class Product:
    pass

# Créer un attribue
class Product:
    nb_products = 0

print(Product.nb_products) # 0

# Créer un nouvel instance
product_1 = Product()

# Créer un attribue d'instance
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Créer un instance avec des attribues
product_1 = Product('iPadPro', 699.99)
product_2 = Product('iPhone12', 799.99)
print(product_1.name) # iPadPro

# Créer un méthode sur l'instance
class Product()
    def display_price(self):
        return f"Price : {self.price}"

print(product_1.display_price())

# Méthode de classe
class Product:
    # ... 
    @classmethod
    def create_default(cls):
        # Créer une instance 
        return cls('Product', 0) # nom par défaut, prix par défaux

product_3 = Product.create_default() 

# Méthode statique
class Product:
    # ... 
    @staticmethod
    def trunc_text(word, nb_char):
        return word[:nb_char] + '...' 

product_3 = Product.trunc_text('This is a blog', 5) # This i... 

# Héritage
class WebProduct(Product):
    def __init__(self, name, price, web_code):
        super().__init__(name, price)
        self.web_code = web_code

# Convention de nom pour variable d'instance 
def __init__(self, price):
    self.__price = price

# Getter et setter
class Product:
    def __init__(self):
        self.__price = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

# Mixins
class Mixin1(object):
    def test(self):
        print "Mixin1"

class Mixin2(object):
    def test(self):
        print "Mixin2"

class MyClass(Mixin2, Mixin1, BaseClass):
    pass

obj = MyClass()
obj.test() # Mixin2
