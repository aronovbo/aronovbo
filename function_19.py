n = int(input())
def factorial(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x



def trailing_zeros(n):
    w = 0
    for i in reversed(str(factorial(n))):
        if int(i) == 0:
            w += 1
        elif int(i) != 0:
            break
    return w
print(trailing_zeros(n))
