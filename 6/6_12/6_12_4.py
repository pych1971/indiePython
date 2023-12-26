N = int(input())
a = []
b = set()
for i in range(N):
    a.append(list(map(int, input().split())))
    b.update(a[i])
print(len(set(b)))
