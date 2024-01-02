n = int(input())
t = {}
for i in range(n):
    a = input().split()
    if a[1] in t.keys():
        t[a[1]] += ' ' + a[0]
    else:
        t[a[1]] = a[0]
m = int(input())
z = []
for i in range(m):
    z.append(input())
for i in z:
    if i in t.keys():
        print(t[i])
    else:
        print('Неизвестный номер')
