n = int(input())
a = []
x = "Yes"
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            x = "No"
            break
print(x)
