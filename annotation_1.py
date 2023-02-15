letter = input()
shift = int(input())
def shift_letter(letter : str, shift: int):
    s = ord(letter) + shift
    if ord(letter) + shift > 122:
        s = 96 + shift
        d = s - 122
        f = 96 + d

    return chr(f)
print(shift_letter(letter,shift))
