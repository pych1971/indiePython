n = int(input())
a = {}
name = []
for i in range(n):
    name.append(input())
for i in range(n):
    if name[i] not in a.values():
        a[i] = name[i]
        print('OK')
    else:
        for j in range(1, i + 1):
            if (x := name[i] + str(j)) not in a.values():
                a[i] = x
                break
        print(a[i])
