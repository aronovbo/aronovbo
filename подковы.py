n = list(map(int,input().split()))

m = set(n)

if len(m) <= len(n):
    print(len(n) - len(m))
