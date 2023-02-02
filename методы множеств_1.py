s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

print(s1, s2)

sn = s1.intersection(s2)
sn = sorted(sn)
print(*sn)
