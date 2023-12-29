def count_AGTC(dna):
    d = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
    c = []
    for i in dna:
        d[i] += 1
    for i in ('AGTC'):
        c.append(d[i])
    return tuple(c)


# код ниже не стоит удалять, он нужен для проверки
assert count_AGTC('AGGTC') == (1, 2, 1, 1)
assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
assert count_AGTC('CCT') == (0, 0, 1, 2)
print('Проверки пройдены')
