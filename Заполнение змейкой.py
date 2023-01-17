#
# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     if i % 2 != 0:
#         a.append([str(j + i*m).ljust(2) for j in range(m)])
#         a[i].reverse()
#     else:
#         a.append([str(j + i*m).ljust(2) for j in range(m)])
#     print(*a[i])


n, m = map(int, input().split())
a = []
for i in range(n):
    if i % 2 != 0:
        a.append([str(j + i*m) for j in range(m)])
        a[i].reverse()
    else:
        a.append([str(j + i*m) for j in range(m)])
    print(*a[i])
print(a)