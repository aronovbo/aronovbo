n = int(input())
s = []
for i in range(1, n+1):
    s.append([i, input()])
print('OK')
n = 0
for i in range(1,len(s)):
    if s[0][1] == s[i][1]:
        n += 1
        s[i][1] = s[i][1] + str(n * 1)
        print(s[i][1])
    elif s[0][1] != s[i][1]:

        print('OK')

print(s)











