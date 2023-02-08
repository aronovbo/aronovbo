a = [1,2,2,3,4,4,5,6]
d = []
for j in a:
    if j not in d:
        d.append(j)
print(d)