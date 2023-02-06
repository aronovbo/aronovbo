


# def sum_num():
#     z = []
#     for i in input():
#         if i.isdigit():
#             z.append(int(i))
#     print(sum(z))
# sum_num()

# def sum_num():
#     s = input()
#     j = 0
#     for i in s:
#         if i.isdigit():
#             j += int(i)
#     print(j)
# sum_num()

# def sum_num():
#
#     j = 0
#     for i in input():
#         if i.isdigit():
#             j += int(i)
#     print(j)
# sum_num()

def sum_num (s):
    n = 0
    for i in range(len(s)):
        if s[i].isdigit():
            n += int(s[i])
    print(n)
sum_num(s)