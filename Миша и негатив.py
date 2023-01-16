n, m = map(int, input().split())
a = [input() for i in range(n)]
input()
d = [input() for j in range(n)]

print(a)
print(d)
c = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == d[i][j]:
            c += 1
print(c)




# n, m = map(int, input().split())
#
# a = [(input()) for a in range(n)]
# print(input())
# d = [(input()) for d in range(n)]

# b = []
# c = []
# for i in range(n):
#     for j in a[i]:
#         b.append(j)
# print(b)
#
# for i in b:
#     if i == 'W':
#         i = 'B'
#     elif i == 'B':
#         i = 'W'
#     c.append(i)
# print(c)
