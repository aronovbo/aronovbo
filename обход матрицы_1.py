a = []
n = int(input())
m = n

for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        print(a[j][i], end=' ')
    print()






