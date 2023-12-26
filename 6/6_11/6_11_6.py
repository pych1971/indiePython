N = int(input())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
for i in range(N):
    print(len(set(a[i])))
