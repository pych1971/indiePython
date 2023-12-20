n, m = map(int, input().split())
p = []
c = '#Black&White'
for i in range(n):
    p.append(input())
for i in range(n):
    for j in range(m):
        if p[i][j] == 'C' or p[i][j] == 'M' or p[i][j] == 'Y':
            c = '#Color'
            break
print(c)
