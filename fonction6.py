def Fibonacci(n):
    list = []
    list.append(1)
    list.append(1)

    x=0
    while x<n:
        chiffre1 = list[-1]
        chiffre2 = list[-2]
        list.append(chiffre1+chiffre2)
        x+=1

    return list

print(Fibonacci(10))
