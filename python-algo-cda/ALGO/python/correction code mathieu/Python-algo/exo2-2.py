# Votre script prend une liste de notes en entrée, indiquez la moyenne de la liste.

notes = [12, 10, 20, 8, 15, 18,15,12]
somme = 0
#nb_note = len(notes)
nb_note_bis = 0
#print(nb_note)

for valeur in notes:
    nb_note_bis = nb_note_bis + 1

print("Nb elem tableau : " + str(nb_note_bis))
for note in notes:
    #print(note)
    somme = somme + note

moyenne = somme/nb_note_bis
print("La moyenne est de : " + str(moyenne))