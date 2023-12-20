n = int(input())
s = list(map(int, input().split()))
p = 0
x = True
while x:
    x = False
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            s[i], s[i + 1] = s[i + 1], s[i]
            p += 1
            x = True
for j in range(len(s)):
    print(s[j], end=' ')
print()
print(p)
