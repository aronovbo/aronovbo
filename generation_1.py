# import random
#
# a = [random.randint(-5, 5) for i in range(5)]
# print(a)
# b = [abs(j) for j in a]
# print(b)
# c = [j**2 for j in b if j % 2 == 0]
# print(c)

# bo = input().split()
# bo = [int(i) for i in bo]
# print(bo)

# n = 4
# m = 5
#
# a = [['+'*3] * m for i in range(n)]
# for j in a:
#     a[0][3] = 'bo'
#     a[3][0] = 'aronov'
#     print(j)

# a = [[i, j, k] for i in 'aronov' for j in 'boris' for k in 'alex' if i == k]
# print(a)


# a = [i**3 for i in range(1,11)]
# print(a)

# a, b = map(int, input().split())
# a, b = [int(i) for i in input().split()]
#
# if a <= b:
#     c = [i ** 2 for i in range(a, b+1)]
# else:
#     c = [i ** 3 for i in range(a, b - 1, -1)]
# print(c)

# st = 'Create a list of the first letters of every word in this string'
# st = st.split()
# print(st)
# w = [i[0] for i in st]
# print(w)

# from string import ascii_uppercase
# # print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
# s = ascii_uppercase
# # print(s)
# n = int(input())
# #
# a = [i for i in s]
# print(a[:n])

# from string import ascii_uppercase
# s = ascii_uppercase
# n = int(input())
# a = [s[i] * (i + 1) for i in range(n)]
# print(a[:n])

phrase = 'Take only the words that start with t in this sentence'
s = phrase.split()
# print(s)

a = [i for i in s if i[0] == 't' or i[0] == 'T']
print(a)
print(id(a))

