n = int(input())
a = []
m = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    if a[i][n - i - 1] > m:
        m = a[i][n - i - 1]
print(m)
