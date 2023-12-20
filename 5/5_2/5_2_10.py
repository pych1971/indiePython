n=int(input())
mwin=0
cwin=0
for i in range(n):
    m,c=map(int,input().split())
    if m>c:
        mwin+=1
    elif m<c:
        cwin+=1
if mwin>cwin:
    print('Mishka')
elif mwin<cwin:
    print('Chris')
else:
    print('Friendship is magic!^^')
