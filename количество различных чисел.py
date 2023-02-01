n = int(input())
s = [input().split() for i in range(n)]

m = set()
for i in s:
    m.update(i)
print(len(m))
