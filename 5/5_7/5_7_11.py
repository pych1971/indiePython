n, m = map(int, input().split())
a = []
b = []
bestR = 0
bestS = 0
num = 0
for i in range(n):
    a.append(list(map(int, input().split())))
    b.append([0] * 2)
for i in range(n):
    for j in range(m):
        b[i][0] += a[i][j]
        if a[i][j] > b[i][1]:
            b[i][1] = a[i][j]
        if i == 0:
            bestR = b[i][1]
            bestS = b[i][0]
    if b[i][1] > bestR:
        num = i
        bestR = b[i][1]
        bestS = b[i][0]
    elif b[i][1] == bestR and b[i][0] > bestS:
        num = i
        bestS = b[i][0]
print(num)
