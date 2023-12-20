n, m = map(int, input().split())
a = []
s = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    s = 0
    for j in range(m):
        s += a[i][j]
    print(s, end=" ")
print()
for j in range(m):
    s = 0
    for i in range(n):
        s += a[i][j]
    print(s, end=" ")
