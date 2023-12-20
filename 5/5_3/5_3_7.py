a=list(map(int, (input().split())))
x=0
for i in range(len(a)):
    if a[i]>0:
        x=a[i]
        break
for i in range(len(a)):
    if a[i]>0 and x>a[i]:
        x=a[i]
if x>0:
    print(x)
else:
    print('Empty')
