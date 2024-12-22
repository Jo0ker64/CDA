mot = input("Votre mot : ")
tom = ''.join(reversed(mot))
if (mot == tom):
    print('Palindrome ! ' + mot + ' = ' + tom)
else:
    print(mot + ' n\'est pas un palindrome ! Car ' + mot + ' != ' + tom)