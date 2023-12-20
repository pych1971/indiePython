n, x = map(int, input().split())
s = 0
for i in range(n):
    for j in range(n):
        if i == j and (i + 1) ** 2 == x:
            s += 1
        elif i > j and (i + 1) * (j + 1) == x:
            s += 2
print(s)
