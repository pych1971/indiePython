a = []
with open('words.txt', encoding='utf-8') as f:
    x = f.readlines()
    for i in x:
        if i.strip()[-2:].upper() == 'ЕЯ':
            if i.strip().upper() not in a:
                a.append(i.strip().upper())
    a.sort(key=lambda x: (len(x), x))
    for i in a:
        print(i)
