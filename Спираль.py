n = int(input())
a = []
for i in range(n):
    a.append([((j+1) ** 2) for j in range(n)])
    break
print(a)