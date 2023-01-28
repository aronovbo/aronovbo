s = input().lower().strip()
d = {}
for i in s:
    if i in d and i.isalpha():
        d[i] += 1
    elif i not in d and i.isalpha():
        d[i] = 1

print(d)


