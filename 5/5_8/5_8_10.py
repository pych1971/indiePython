r, c = map(int, input().split())
a = []
s = 0
for i in range(r):
    a.append(input())
for i in range(r):
    if 'S' in a[i]:
        continue
    else:
        s += c
        a.pop(i)
        a.insert(i, [0] * c)
for j in range(c):
    SS = 0
    TT = 0
    for i in range(r):
        if a[i][j] == 'S':
            SS += 1
        elif a[i][j] == '.':
            TT += 1
    if SS == 0:
        s += TT
print(s)
