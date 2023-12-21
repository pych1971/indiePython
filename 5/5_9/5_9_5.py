a, b = map(int, input().split())
if a <= b:
    c = [i ** 2 for i in range(a, b + 1)]
elif a > b:
    c = [i ** 3 for i in range(a, b - 1, -1)]
print(c)
