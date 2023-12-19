n, m = map(int, input().split())
a = []
best = 0
sportx = 0
sporty = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if a[i][j] > best:
            best = a[i][j]
            sportx = i
            sporty = j
print(best)
print(sportx, sporty)
