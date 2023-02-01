n = int(input())
# print(len(set(input().split() for i in range(n))))

s = [input().split() for i in range(n)]
print(s)
for i in s:
    print(len(set(i)))



