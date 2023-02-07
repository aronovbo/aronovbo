def generate_fizz_buzz_list(n):
    x = []
    for i in range(1, n+1):

        if i % 3 == 0 and i % 5 == 0:
            x.append('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            x.append('Fizz')
        elif i % 5 == 0 and i % 3 != 0:
            x.append('Buzz')
        elif i % 5 != 0 and i % 3 != 0:
            x.append(i)
    return x
a = generate_fizz_buzz_list(10)
print(a)
