print("Entre un chiffre")
chiffre = input()

def doubleNumber(chiffre):
    if chiffre.isnumeric():
        chiffre = int(chiffre)*2
        return chiffre
    else :
        return "Ce n'est pas un chiffre ou un nombre"

print(doubleNumber(chiffre))
