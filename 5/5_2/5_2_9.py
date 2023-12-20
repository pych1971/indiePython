n=int(input())
s=1
if n==1 or n==0:
    print(1)
elif n>1:
    for i in range(1,n+1):
        s*=i
    print(s)
