n = int(input())
a = []
s = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][1] == a[j][0] and i != j:
            s += 1
print(s)
