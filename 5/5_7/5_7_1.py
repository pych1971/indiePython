n = int(input())
a = []
s = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    s += a[i][i]
print(s)
