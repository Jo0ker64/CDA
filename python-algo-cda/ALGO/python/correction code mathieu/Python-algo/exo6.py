# Votre script demande un mot en entrée, indiquez si le mot est un palindrome ou non
# Kayak

mot = input("Votre mot : ")
mot_inverser = "".join(reversed(mot))

print(mot)
print(mot_inverser)

if (mot == mot_inverser):
    print('Palindrome !')
else:
    print('Pas palindrome !')