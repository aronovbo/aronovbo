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


a = [i**3 for i in range(1,11)]
print(a)

