a = []
b = []
c = []
n, m = (map(int,input().split()))
for i in range(n):
    a.append(list(map(int,input().split())))
    b.append(max(a[i]))
    c.append(sum(a[i]))

print(b)
print(c)
print(max(b))
print(max(c))

if b.count(max(b)) == 1:
    print(b.index(max(b)))
elif b.count(max(b)) > 1:


    if c.count(max(c)) == 1:

        print(b.index(max(b)))
    # elif
        # print(c[b.index(max(b))])
        # print(c.index(max(c)))
    # elif c.count(max(c)) > 1:
    #     print(0)

# print(b.index(max(b)), a[b.index(max(b))].index(max(b)))
# 3 3
# 6 2 7
# 1 2 8
# 1 3 8