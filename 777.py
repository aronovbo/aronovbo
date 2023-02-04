# my_frozen = ['7']
# for i in my_frozen:
#     while len(my_frozen) <= 76:
#         i += '7'
#         my_frozen.append(i)
#
# my_frozen = frozenset(my_frozen)
# print(my_frozen)

# my_frozen = frozenset(int(i * '7') for i in range(1, 78))
#
# print(my_frozen)
person = {"name": "Jack", "age": 21, "Country": "India"}

frozen_dict = frozenset(person)
print(f'{frozen_dict=}')

a = frozen_dict.copy()

print(f'{a=}')