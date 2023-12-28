def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
x = []
y = []
for i in range(n):
    x.append(int(input()))
for i in range(0, n - 1):
    for j in range(i + 1, n):
        y.append(gcd(x[i], x[j]))
print(min(y))
