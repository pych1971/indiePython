a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = list(a.intersection(b))
c.sort()
for i in range(len(c)):
    print(c[i], end=' ')
