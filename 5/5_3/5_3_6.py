a=list(map(int, (input().split())))
x=int(input())
for i in range(len(a)):
    if a[i]==x:
        print(i+1)
        break
else:
    print('ErrorValue')
