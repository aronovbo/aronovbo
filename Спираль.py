n = int(input())

a = [[0] * n for i in range(n)]
i = 1
x = 0
y = -1
mr = 0
mc = 1
l = len(str(n ** 2))
while i <= n ** 2:
    if 0 <= x+mr < n  and 0 <= y + mc < n and a[x+mr][y+mc] == 0:
        x += mr
        y += mc
        a[x][y] = i
        i += 1
    else:
        if mc == 1:
            mc = 0
            mr = 1
        elif mr == 1:
            mr = 0
            mc = -1
        elif mc == -1:
            mr = 0
            mr = -1
        elif mr == -1:
            mr = 0
            mc = 1
for i in a:
    for j in i:
        print(str(i).rjust(l), end=' ')
    print()


