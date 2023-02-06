def is_between(a, b, c):
    if b <= c:
        if b <= a <= c:
            print('True')
        else:
            print('False')
    if b >= c:
        if c <= a <= b:
            print('True')
        else:
            print('False')

is_between(5, 9, 1)
