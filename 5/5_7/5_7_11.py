n, m = map(int, input().split())
a = []
b = []
best = 0
for i in range(n):
    a.append(list(map(int, input().split())))
    b.append([0] * 2)
