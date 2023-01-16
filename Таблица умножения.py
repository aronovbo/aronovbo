n, m = map(int, input().split())
c = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j,'*', i, '=', j * i)
        if j * i == m:
            c += 1
print(c)
