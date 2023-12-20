n,k=map(int, input().split())
i=0
s=0
while (s:=s+5*i)+k<240 and i<n:
    i+=1
if s+k>240:
    i-=1
print(i)
