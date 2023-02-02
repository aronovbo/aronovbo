s = input().lower().split(',')
d = set()

for i in s:
    if i not in d:
        d.add(i)
        print('НЕТ')
    else:
        print('ДА')

