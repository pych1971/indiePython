n=int(input())
s=0
i=0
vsego=0
while vsego<n:
    i+=1
    s+=i
    vsego+=s
if vsego>n:
    i-=1
print(i)
