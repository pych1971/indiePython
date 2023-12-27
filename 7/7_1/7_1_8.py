def count_letters(a):
    N = 0
    K = 0
    for i in range(len(a)):
        if 'A' <= a[i] <= 'Z' or 'А' <= a[i] <= 'Я':
            N += 1
        elif 'a' <= a[i] <= 'z' or 'а' <= a[i] <= 'я':
            K += 1
    print(f'Количество заглавных символов: {N}')
    print(f'Количество строчных символов: {K}')
