voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
nb_voyelles = 0
for lettre in input("Votre mot : "):
    #print(lettre)
    if (lettre in voyelles):
        #print('voyelle trouvée : ' + lettre)
        nb_voyelles += 1
print(nb_voyelles)