n = 4
m = 4
a = []

for i in range(n):
    a.append(input())

# print(a)
for i in range(n-1):
    for j in range(m-1):
        print(a)
        if a[i][j] == a[i][j+1] == a[i+1][j] == a[i+1][j+1]:
            print('No')
        else:
             print('Yes')








