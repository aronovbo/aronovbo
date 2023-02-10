def first_repeated_word(text: str):
    'Находит первый дубль в строке'
    ss = []
    for i in text.split():
        if i not in ss:
            ss.append(i)

        else:
            return i
print(first_repeated_word('bob aro dir'))
