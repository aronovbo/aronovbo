# n = list(map(int, input()))
# print(n)
# print(sum(n))
#
# s = []
# for i in range(len(n)):
#     print(n[i],end=' ')
#     if i % 2 == 0:
#         n[i+1] *= 2
#         if n[i+1] > 9:
#             n[i+1] -= 9
#     s.append(n[i])
# print()
# print(sum(s))
# if sum(s) % 10 == 0:
#     print('True')
# else:
#     print('False')

n = list(map(int, input()))
s = []
# print(n)
# print(sum(n))

for i,j in enumerate(n):
    if i % 2 == 0:
        j *= 2
        if j > 9:
            j -= 9
    s.append(j)
# print(s)
# print(sum(s))

if sum(s) % 10 == 0:
    print('True')
else:
    print('False')




