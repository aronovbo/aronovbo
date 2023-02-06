# объявление функции
def count_letter(text, letter):
    c = 0
    for i in text:
        if i == letter:
            c += 1
    print(c)


# считываем данные
text = input()
symbol = input()
# вызываем функцию
count_letter(text, symbol)
