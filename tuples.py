# a = int(input())
# b = int(input())
#
# c = [i for i in range(a,b+1)]
# c = tuple(c)
# print(c)

# n = int(input())
#
# s = [i for i in range(n, n**2 + 1) if i % 2 != 0]
# s = tuple(s)
# print(s)

# my_tuple = (5,6,7)
# my_tuple = list(my_tuple)
# print(my_tuple)
# my_tuple.reverse()
# print(my_tuple)
# my_tuple = tuple(my_tuple)
# print(my_tuple)

# words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
#                'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
#                'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')
#
# for i in words_tuple:
#         print(f'длина слова {i} = {len(i)}')

my_tuple = (1, 2, 3, 4)
mt = []
for i in my_tuple:
    if i % 2 != 0:
        mt.append(i)

print(sum(mt) / len(mt))
