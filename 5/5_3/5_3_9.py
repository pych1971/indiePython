N=int(input())
S=str(N)
sNechet=0
sChet=0
for i in range(len(S)):
    if i%2==0:
        sChet+=int(S[i])
    else:
        sNechet+=int(S[i])
if (sChet-sNechet)%11==0:
    print('YES')
else:
    print('NO')
