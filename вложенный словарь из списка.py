n = list(map(list, input().split()))
print(n)
n[0].append(n[1])
n[1].append(n[2])
n[2].append(n[3])
# for i in n:
#     i.append(n[int(i)+1])
# n = dict(n)
print(n[:1])

