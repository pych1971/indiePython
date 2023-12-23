S1 = input()
S2 = input()
s2 = {}
s1 = {}
for i in S1:
    s1[i] = s1.get(i, 0) + 1
for i in S2:
    s2[i] = s2.get(i, 0) + 1
if s1 == s2:
    print('YES')
else:
    print('NO')
