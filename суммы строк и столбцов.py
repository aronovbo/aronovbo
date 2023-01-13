a = []
n, m = (map(int,input().split()))
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    ss = 0
    for j in range(m):
        ss += a[i][j]
    print(ss,end=' ')
print()
for j in range(m):
    st = 0
    for i in range(n):
        st += a[i][j]
    print(st,end=' ')





