a = []
x = 'Yes'
for i in range(4):
    a.append(input())
for i in range(3):
    for j in range(3):
        if a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1]:
            x = 'No'
            break
print(x)
