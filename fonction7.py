def FizzBuzz(n):
    x=1
    while x<=n:
        if x%3==0 and x%5==0:
            print("FizzBuzz")
        if x%3==0:
            print("Fizz")
        if x%5==0:
            print("Buzz")
        print(x)

        x=x+1

print(FizzBuzz(100))