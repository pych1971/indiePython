a = list(map(int, input().split()))
x = {}
x[a[-2]] = a[-1]
y = dict(x)
for i in range(len(a) - 3, -1, -1):
    y = dict(x)
    x.clear()
    x[a[i]] = y
print(x)
