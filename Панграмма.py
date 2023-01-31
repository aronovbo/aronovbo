from string import ascii_lowercase
al = ascii_lowercase
al = set(al)

s = input().lower()

ss = set(s)

if ss == al:
    print('YES')
else:
    print('NO')


