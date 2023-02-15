letter = input()
shift = int(input())
def shift_letter(letter : str, shift: int):
    s = chr(ord(letter) + shift)
    return s
print(shift_letter(letter,shift))
