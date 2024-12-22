# Votre script demande lʼâge dʼun utilisateur et vous affichez “majeurˮ ou “mineurˮ

age = input("Votre age : ")

if (int(age) >= 18):
    print('Majeur !')
else:
    print('Mineur !')

print('Vous avez ' + age + ' ans')