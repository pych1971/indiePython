# объявление функции
def replace(text: str, old: str, new: str = ''):
    x = ''
    for i in range(len(text)):
        if text[i] == old:
            x += new
        else:
            x += text[i]
    return x
