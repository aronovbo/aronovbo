a = input()
b = []
for i in a:
    if i.isalpha():
        b.append(i)
b = set(b)
print(len(b))
