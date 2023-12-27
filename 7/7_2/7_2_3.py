# объявление функции
def count_letter(text, letter):
    s = 0
    for i in range(len(text)):
        if letter == text[i]:
            s += 1
    print(s)


# считываем данные
text = input()
symbol = input()
# вызываем функцию
count_letter(text, symbol)
