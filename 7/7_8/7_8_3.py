def rev(n, x):
    if n > 0:
        print(x[-1], end=' ')
        x.pop(-1)
        rev(len(x), x)


n = int(input())
x = list(map(int, input().split()))
rev(n, x)
