n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        a[i][j] = a[i + 1][j] + a[i][j + 1]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()
