n, m = map(int, input().split())
c = 0
a = []
for i in range(n):
    a.append([0] * m)
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            a[i][j] = c
            c += 1
    else:
        for j in range(m - 1, -1, -1):
            a[i][j] = c
            c += 1
for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()
