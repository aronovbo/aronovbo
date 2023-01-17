n = 4

# a = []
# for i in range(n):
#     a.append(input())
a = [(input()) for a in range(n)]

print(a)
for i in range(n-1):
    if a[i] == a[i+1]:
        print("No")
        break
else:
    print('Yes')




