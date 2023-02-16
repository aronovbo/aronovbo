letter = input()
shift = int(input())



def shift_letter(letter : str, shift: int):
    s = ord(letter) + shift
    if shift > 26:
        s = ord(letter) + shift % 26

    # if ord(letter) + shift > 122:
    #     s = 97 + ((ord(letter) + shift) % 26 - 122)
    # elif ord(letter) + shift < 97:
    #     s = 122 - (96 - (ord(letter) + shift))


    return chr(s)
print(shift_letter(letter,shift))
