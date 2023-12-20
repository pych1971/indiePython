a = input().split()
b = []
c = a[:]
for i in range(len(a)):
    c[i] = c[i].lower()
while a != []:
    b.append(a[0])
    a.pop(0)
    c.pop(0)
    while b[-1].lower() in c:
        j = c.index(b[-1].lower())
        a.pop(j)
        c.pop(j)
for i in range(len(b)):
    print (b[i], end=' ')