def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
n = int(input())
s = [input().split() for i in range(n)]

