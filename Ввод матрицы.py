# n = int(input())
# m = int(input())
# a = []
# for i in range(n):
#     a.append([0] * m)
# for i in a:
#     print(i)

n = int(input())
m = int(input())
a = []
for i in range(n):
    b = []
    for i in range(m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)
