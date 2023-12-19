n, m = map(int, input().split())
a = []
s = 0
x = 0
ss = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    ss = 0
    for j in range(m):
        ss += a[i][j]
    if ss > s:
        s = ss
        x = i
print(s)
print(x)
