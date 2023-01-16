n = int(input())
a = [input().split() for i in range(n)]
print(a)

c = 0
for i in a:
    for j in a:
        if i[1] == j[0]:
            c += 1
print(c)




