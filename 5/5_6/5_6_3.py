n = int(input())
p = 2 * n - n - 1
for i in range(n + 1, 2 * n):
    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0:
            p -= 1
            break
print(p)
