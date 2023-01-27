# from pprint import pprint # для красивого вывода словаря
# person = {}
# s = 'IVANOV IVAN 19 Samara SGU 4 5 5 5 4 3 5 3'
#
# s = s.split()
# print(s)
#
# print('-'*15)
#
# person['last_name'] = s[0]
# person['first_name'] = s[1]
# person['age'] = int(s[2])
# person['city'] = s[3]
# person['university'] = s[4]
#
# print(person)
# print('-'*15)
#
# person['marks'] = []
# for i in s[5:]:
#     person['marks'].append(int(i))
#
# pprint(person)

# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
#
# print(sweet["name"])

# days = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }
# print(days[int(input())])

# n = int(input())
# s = [[i,i ** 2] for i in range(1, n+1)]
# print(s)
# s = dict(s)
# print(s)

from string import ascii_lowercase
s = ascii_lowercase
alphabet = []
x = 1
for i in s:
    alphabet.append([i, x])

    x += 1
alphabet = dict(alphabet)
print(alphabet)

# from string import ascii_lowercase as a
# alphabet = {a[i]: i + 1 for i in range(26)}
# print(alphabet)


