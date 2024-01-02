n = int(input())
s = {}
for i in range(n):
    a = input()
    if a in s:
        s[a] += 1
    else:
        s[a] = 1
a = sorted(s.items(), key=lambda x: x[1], reverse=True)
print(f'{a[0][0]}, {a[0][1]}')
print(f'{a[-1][0]}, {a[-1][1]}')
