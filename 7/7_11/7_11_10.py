s = {'Дили': set(), 'Вили': set(), 'Били': set()}
while (a := input()) != 'конец':
    a = a.split(sep=': ')
    s[a[0]].add(a[1])
for key, value in sorted(s.items(), key=lambda x: -len(x[1])):
    print(f'Количество уникальных комментаторов у {key} - {len(value)}')
