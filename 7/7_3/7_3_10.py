def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def trailing_zeros(n):
    fact = factorial(n)
    do = len(str(fact))
    posle = len(str(fact).rstrip('0'))
    x = do - posle
    return x


# код ниже не стоит удалять, он нужен для проверки
assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2
print('Проверки пройдены')
