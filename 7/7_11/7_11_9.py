s = {}
while (a := input()) != 'конец':
    a = a.split(sep=', ')
    if a[0] not in s.keys():
        s[a[0]] = [int(a[1]), 1, int(a[1])]
    else:
        s[a[0]][0] += int(a[1])
        s[a[0]][1] += 1
        s[a[0]][2] = s[a[0]][0] / s[a[0]][1]
for key, value in sorted(s.items(), key=lambda x: (-x[1][2], x)):
    print(key, float(value[2]))
