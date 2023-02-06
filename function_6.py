def count_letters(s):
    x = 0
    y = 0
    for i in list(s):
        if i.isupper():
            x += 1
        elif i.islower():
            y += 1
    print(f'Количество заглавных символов: {x}')
    print(f'Количество строчных символов: {y}')

count_letters('Boris Aronov')