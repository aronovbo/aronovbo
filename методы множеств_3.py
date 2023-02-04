s = input()
d = []
d2 = set()
for i in s:
    if i.isdigit() and s.count(i) > 1:
        d.append(i)

d = set(d)
d = sorted(d)
if len(d) >= 1:
    print(*d)
else:
    print('NO')





