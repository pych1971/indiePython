a = []
for i in range(5):
    a.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            x = i
            y = j
s = abs(x - 2) + abs(y - 2)
print(s)
