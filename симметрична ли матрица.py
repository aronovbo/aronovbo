# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]

n = int(input())
m = n
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
flag = True
for i in range(n):
    if not flag:
        break
    for j in range(m):
        if i != j and a[i][j] != a[j][i]:
            flag = False
            break
print('Yes' if flag else 'No')












# 0 1 2
# 1 5 3
# 2 3 4