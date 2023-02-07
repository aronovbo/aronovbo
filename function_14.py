def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
n = int(input())
s = [input().split() for i in range(n)]
r = []

for i in s:
    r.append(int(*i))
q = max(r)
w = min(r)



e = gcd(q, w)
print(e)
