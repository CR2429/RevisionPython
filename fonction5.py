print("Entre 2 chiffre")
chiffre1 = input("Chiffre 1: ")
chiffre2 = input("Chiffre 2: ")

def Addition(chiffre1, chiffre2):
    if chiffre1.isdigit() and chiffre2.isdigit():
        sum = int(chiffre1) + int(chiffre2)
        return sum
    else:
        return "Une des deux valeur est pas un nombre"

print(Addition(chiffre1, chiffre2))