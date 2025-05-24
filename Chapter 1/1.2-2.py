for i in range(1, 51):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if i > 1 and isPrime:
        print("Prime")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
