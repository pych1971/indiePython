l1,l2=map(int, input().split())
s1=list(map(int, input().split()))
s2=list(map(int, input().split()))
s=[]
while len(s1)>=1 or len(s2)>=1:
    if len(s1)==0:
        s.append(s2[0])
        del s2[0]
    elif len(s2)==0:
        s.append(s1[0])
        del s1[0]
    elif s1[0]<=s2[0]:
        s.append(s1[0])
        del s1[0]
    elif s2[0]<=s1[0]:
        s.append(s2[0])
        del s2[0]
i=0
while i<(len(s)):
    print(s[i], end=' ')
    i+=1
#print(s)