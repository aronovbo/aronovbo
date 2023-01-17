n, m = map(int, input().split())
a = []
for i in range(n):
    if i % 2 != 0:
        a.append([str(j + i*m) for j in range(m)])
    else:
        a.append([str(j + i * m) for j in range(m)])
    print(*a[i])
