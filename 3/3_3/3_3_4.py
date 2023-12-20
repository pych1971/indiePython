a,b,c=map(int, input().split())
if a>b:
    if b>c:
        print (a-c)
    else:
        if a>c:
            print(a-b)
        else:
            print(c-b)
else:
    if b<c:
        print(c-a)
    else:
        if a<c:
            print(b-a)
        else:
            print(b-c)