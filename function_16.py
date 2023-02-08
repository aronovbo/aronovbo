lst = [2, 1, 1, 1, 1, 1, 2, 2, 2, 2]
# print(lst)
def find_duplicate(lst):
    s = []

    for i in lst:
        if lst.count(i) > 1:
            s.append(i)

    # print(s)
    q = []
    for j in s:
        if j not in q:
            q.append(j)
    print(q)


find_duplicate(lst)

