a = input()
b = set()
c = ''
for i in range(len(a)):
    if a[i] not in b:
        b.add(a[i])
        c += a[i]
print(str(c))
