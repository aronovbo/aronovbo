a = []
n, m = (map(int,input().split()))
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m-1,-1,-1):

        print(a[i][j], end=' ')
    print()