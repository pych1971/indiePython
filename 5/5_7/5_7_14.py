x, y = map(int, input().split())
s = 0
a = []
b = []
for i in range(x):
    a.append(input())
input()
for i in range(x):
    b.append(input())
for i in range(x):
    for j in range(y):
        if a[i][j] == b[i][j]:
            s += 1
print(s)
