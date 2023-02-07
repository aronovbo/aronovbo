def factorial(n):
    x = []
    for i in range(1, n+1):
        print(i)

        if i // 3 == 1 and i // 5 == 1:
            x.append('FizzBuzz')
        elif i // 3 == 1 and i // 5 != 1:
            x.append('Fizz')
        elif i // 5 == 1 and i // 3 != 1:
            x.append('Buzz')
        elif i // 5 != 1 and i // 3 != 1:
            x.append(i)
    return x
a = factorial(4)
print(a)
