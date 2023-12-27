# объявление функции
def is_between(a, b, c):
    if min(b, c) <= a <= max(b, c):
        print('True')
    else:
        print('False')


# считываем данные
a, b, c = map(int, input().split())

# вызываем функцию
is_between(a, b, c)
