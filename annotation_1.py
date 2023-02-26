def shift_letter(letter : str, shift: int):
    'Функция сдвигает символ letter на shift позиций'
    s = (ord(letter) - 97 + shift) % 26 + 97
    return chr(s)

