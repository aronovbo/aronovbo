n = list(map(int, input()))
# print(n)
s = []
for i in range(len(n)):
    # print(n[i])
    if i % 2 == 0:
        n[i+1] *= 2
    s.append(n[i])
print(s)


