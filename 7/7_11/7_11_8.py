n = int(input())
t = {}
for i in range(n):
    a = input().split()
    if a[2] in t.keys():
        t[a[2]] += [a[0]]
    else:
        t[a[2]] = [a[0]]
for i in t.keys():
    t[i] = sorted(t[i])
m = int(input())
z = []
for i in range(m):
    z.append(input())
for i in z:
    if i in t.keys():
        x = ''
        for j in range(len(t[i])):
            if x == '':
                x = t[i][j]
            else:
                x += ' ' + t[i][j]
        print(x)
    else:
        print('Нет данных')
