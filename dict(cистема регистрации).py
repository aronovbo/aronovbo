# n = int(input())
# s = []
# for i in range(1, n+1):
#     s.append([i, input()])
# print(s)
# print('OK')
# n = 0
# m = 0
# for i in range(1,len(s)):
#     if s[0][1] == s[i][1]:
#         n += 1
#         s[i][1] = s[i][1] + str(n * 1)
#         print(s[i][1])
#     elif s[0][1] != s[i][1] and s[i][1] not in s:
#         print('OK')
#     elif s[0][1] != s[i][1] and s[i][1] in s:
#         m += 1
#         s[i][1] = s[i][1] + str(m * 1)
#         print(s[i][1])
#
# print(s)

ls = {}
n = int(input())
for i in range(n):
    l = input()
    if l in ls:
        print(f'{l}{ls[l]}')
        ls[l] += 1
    else:
        print('OK')
        ls[l] = 1






