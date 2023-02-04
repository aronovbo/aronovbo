s = input()
print(s)
d = []

for i in s:
    if i not in d:
        d.append(i)
print(*d,sep='')




