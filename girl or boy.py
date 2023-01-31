name = input().lower()
print(name)

s = set(name)
if len(s) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
