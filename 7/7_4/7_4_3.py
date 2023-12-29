def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    x = ''
    if shift > 26 or shift < -26:
        shift %= 26
    if ord(letter) + shift > 122:
        x = 96 + shift - (122 - ord(letter))
    elif ord(letter) + shift < 97:
        x = 122 + shift + (ord(letter) - 96)
    else:
        x = ord(letter) + shift
    return chr(x)
