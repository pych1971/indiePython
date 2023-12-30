def print_goods(*args):
    a = []
    for i in args:
        if type(i) == str and i != '':
            a.append(i)
    if a == []:
        print('Нет товаров')
    else:
        for i in range(len(a)):
            print(f'{i + 1}. {a[i]}')
