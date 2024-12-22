# SYNTAXE IF
age = 64
prenom = "Mathieu"
print(age)
print(prenom)
if (age < 18):
    print("Mineur")
elif (age >= 18 and age < 64):
    print("Majeur")
else:
    print('Retraité')

# boucle for
for nb in range(1,101):
    print(nb*10)