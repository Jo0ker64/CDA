# Votre script demande 1 nombre en entrée et vous retournez “pairˮ ou “impairˮ

nb = int(input("Votre nb : "))
print(type(nb)) # VERIFICATION
print(type(nb) == str) # <===== CONDITION
print(type(nb) == int) # if = test | print = affichage
# Test le type de retour utilisateur
# en fonction du type type non reconnu : str
# Si type int affiche pair ou impair

if (type(nb) == int):
    if (nb%2 == 0):
        print('Pair !')
    else:
        print('Impairs')
elif (type(nb) == str):
    print('Entrer un nombre et pas un mot')
