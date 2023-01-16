n, m = map(int, input().split())
a = []

for i in range(n):
    a.append('.' + input() + '.')
# print(a)
a.append('.' * (n + 2))
a.insert(0, '.' * (m + 2))

# print(a)
c = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j] == a[i][j+1] == a[i][j-1] == a[i-1][j] == a[i+1][j] == '.':
            c += 1
print(c)


# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()





    #     print(a[i][j], end=' ')
    # print()
