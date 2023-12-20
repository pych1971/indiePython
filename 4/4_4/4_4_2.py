n=int(input())
i=1
a=[]
s=0
while i**2<=n:
    if n%i==0:
        s+=i
        if i!=n//i:
            s+=n//i
    i+=1
print(s)
