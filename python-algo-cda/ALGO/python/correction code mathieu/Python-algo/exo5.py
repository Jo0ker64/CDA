# Votre script demande un mot a lʼutilisateur en entrée, indiquez le nombre de voyelle que le
# mot contient

voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
mot = input("Votre mot : ")
resultat = 0
#print(mot.lower())
#print(mot.upper())
for lettre in mot.lower():
    #print(lettre)
    if (lettre in voyelles):
        #print(lettre)
        resultat += 1 # resultat = resultat + 1

print("Nb de voyelles : " + str(resultat))