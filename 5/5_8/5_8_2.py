n = int(input())
a, b, c = map(int, input().split())
x = []
for i in range(n):
    x.append([0] * n)
for i in range(n):
    for j in range(n):
        if j > i:
            x[i][j] = a
        elif i > j:
            x[i][j] = b
        else:
            x[i][j] = c
for i in range(n):
    for j in range(n):
        print(x[i][j], end=" ")
    print()
