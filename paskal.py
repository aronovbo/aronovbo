n = int(input())

t = []

for i in range(n + 1):
    t.append([1] + [0] * 4)

# for i in t:
#     print(i)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        t[i][j] = t[i-1][j] + t[i-1][j-1]

# for i in t:
#     print(i)
for i in range(0, n + 1):
    for j in range(0, i + 1):
        print(t[i][j], end=' ')
    print()