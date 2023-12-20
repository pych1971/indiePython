n, m = map(int, input().split())
a = []
s = 0
a.append('.' * (m + 2))
for i in range(n):
    a.append('.' + input() + '.')
a.append('.' * (m + 2))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j] == a[i - 1][j] == a[i][j - 1] == a[i + 1][j] == a[i][j + 1] == '.':
            s += 1
print(s)
