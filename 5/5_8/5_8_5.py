n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(1, m):
        a[i][j] = a[i - 1][j] + a[i][j - 1]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()
