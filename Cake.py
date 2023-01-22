r, c = map(int, input().split())
cake = []
for i in range(r):
    cake.append(input())
# print(cake)

m = [[False] * c for i in range(r)]
# print(m)
for i in range(r):
    if 'S' not in cake[i]:
        for j in range(c):
            m[i][j] = True
# print(m)

for j in range(c):
    y = False
    for i in range(r):
        if cake[i][j] == 'S':
            y = True
            break
    if not y:
        for i in range(r):
            m[i][j] = True
c = 0
for i in m:
    c += i.count(True)
print(c)


