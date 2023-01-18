n, m = map(int, input().split())


a = []
b = []
for i in range(n):
    a.append(input().split())
print(a)

for j in a:
    for k in j:
        b.append(k)
print(b)
if 'C' and 'M' and 'Y' in b:
    print('#Color')
else:
    print('#Black&White')
