a = input()
b = set()
c = set()
for i in range(len(a)):
    if '0' <= a[i] <= '9':
        if a[i] in b:
            c.add(a[i])
        else:
            b.add(a[i])
d = list(c)
d.sort()
if c == set():
    print('NO')
else:
    for i in range(len(d)):
        print(int(d[i]), end=' ')
