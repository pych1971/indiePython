n = int(input())
s = list(map(int, input().split()))
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if j==0 and s[i]<s[j] or s[j-1]<=s[i]<s[j]:
            x = s[i]
            s.pop(i)
            s.insert(j, x)
            break
for i in range(n):
    print(s[i], end=' ')