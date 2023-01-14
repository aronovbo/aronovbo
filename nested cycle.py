# for i in range(3):
#     for j in range(5):
#         print('*', end=' ')
#     print()

# for i in range(3):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# 0 0 0 0 0
# 1 1 1 1 1
# 2 2 2 2 2

# for i in range(3):
#     for j in range(5):
#         print(j, end=' ')
#     print()

# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4

for i in range(3):
    for j in range(i):
        print(j, end=' ')
    print()


# 0
# 0 1

for i in range(1, 10):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# 0
# 0 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9

