
letter = input()
shift = int(input())
def shift_letter(letter : str, shift: int):
    'Функция сдвигает символ letter на shift позиций'
    s = (ord(letter) - 97 + shift) % 26 + 97
    return chr(s)


def caesar_cipher(letter, shift_letter):
    text2 = []
    for i in letter:
        if i.isalpha():
            shift_letter(i, shift)
    text2.append(i)
    return text2

print(caesar_cipher(text,shift_letter()))

