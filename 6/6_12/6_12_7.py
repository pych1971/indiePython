a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = list(a.difference(b))
c.sort()
for i in range(len(c)):
    print(c[i], end=' ')
