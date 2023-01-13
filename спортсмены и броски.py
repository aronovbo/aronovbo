a = []
s = []
n, m = (map(int,input().split()))
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    ss = 0
    for j in range(m):
        ss += a[i][j]
        s.append(s)
print(max(s))


