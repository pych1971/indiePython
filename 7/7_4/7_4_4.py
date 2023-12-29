def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    x = ''
    if shift > 26 or shift < -26:
        shift %= 26
    if ord(letter) + shift > 122:
        x = ord(letter) + shift - 26
    elif ord(letter) + shift < 97:
        x = ord(letter) + shift + 26
    else:
        x = ord(letter) + shift
    return chr(x)


def caesar_cipher(phrase: str, shift: int) -> str:
    'Шифр цезаря'
    newPhrase = ''
    for i in range(len(phrase)):
        if 'a' <= phrase[i] <= 'z':
            newPhrase += shift_letter(phrase[i], shift)
        else:
            newPhrase += phrase[i]
    return newPhrase
