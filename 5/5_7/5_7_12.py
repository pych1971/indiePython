n, m = map(int, input().split())
a = []
bestR = 0
s = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if a[i][j] > bestR:
            bestR = a[i][j]
for i in range(n):
    if bestR in a[i]:
        s += 1
print(s)
