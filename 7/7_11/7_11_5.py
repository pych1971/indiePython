s = {}
i = 0
while (a := input()) != 'конец':
    s[a.split(sep=': ')[0]] = int(a.split(sep=': ')[1])
    i += 1
for key, value in sorted(s.items(), key=lambda x: x[1], reverse=True):
    print(key)
