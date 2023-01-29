# s1 = input()
# s2 = input()
# d1 = {}
# d2 = {}
#
#
# for i in s1:
#     if i in s2:
#
#         d1.setdefault(i, )
#         d1[i] += 1
# print(d1)
# for j in s2:
#
#     d2.setdefault(j, )
#     d2[j] += 1
#
#
# if d1 == d2:
#     print('YES')
# else:
#     print('NO')

s1 = input()
d1 = {}
for i in s1:
    if i in d1:
        d1[i] += 1
    elif i not in d1:
        d1[i] = 1

s2 = input()
d2 = {}
for j in s2:
    if j in d2:
        d2[j] += 1
    elif j not in d2:
        d2[j] = 1

print(d1)
print(d2)

if d1 == d2:
    print('YES')
else:
    print('NO')

