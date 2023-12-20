a = list(map(int, input().split()))
for i in range(len(a)):
    for j in range(1, a[i]+1):
        print('*', end='')
    print()
