n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
i=0
a.sort(reverse=True)
b.sort(reverse=True)
while len(a)>=1 and len(b)>=1:
    if -1<=(a[0]-b[0])<=1:
        del a[0]
        del b[0]
        i+=1
    elif a[0]-b[0]>1:
        del a[0]
    elif b[0]-a[0]>1:
        del b[0]
print(i)
