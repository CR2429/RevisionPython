liste_nombre_premier = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print("Entre un nombre entre 1 et 100")
chiffre = input()

def isPrime(chiffre):
    if chiffre.isnumeric() == False:
        return False
    if int(chiffre) in liste_nombre_premier:
        return True
    else:
        return False

print(isPrime(chiffre))