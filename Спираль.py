# n = int(input())
#
# a = [[0] * n for i in range(n)]
# i = 1
# x = 0
# y = -1
# mr = 0
# mc = 1
# l = len(str(n ** 2))
# while i <= n ** 2:
#     if 0 <= x+mr < n  and 0 <= y + mc < n and a[x+mr][y+mc] == 0:
#         x += mr
#         y += mc
#         a[x][y] = i
#         i += 1
#     else:
#         if mc == 1:
#             mc = 0
#             mr = 1
#         elif mr == 1:
#             mr = 0
#             mc = -1
#         elif mc == -1:
#             mc = 0
#             mr = -1
#         elif mr == -1:
#             mr = 0
#             mc = 1
# for i in a:
#     for j in i:
#         print(str(j).rjust(l), end=' ')
#     print()
#
#
# put your python code here
n = int(input())
lst = [[0] * n for i in range(n)]
i, j, di, dj = 0, 0, 0, 1
for k in range(n * n):
    lst[i][j] = k + 1
    if lst[(i + di) % n][(j + dj) % n]:
        di, dj = dj, -di
    i, j = i + di, j + dj
for line in lst:
    print(*line)