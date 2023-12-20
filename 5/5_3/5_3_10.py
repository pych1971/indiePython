a=input()
x=0
s=0
for i in range(len(a)):
    if '0'<=a[i]<='9':
        x+=1
        s+=int(a[i])
print(x, s)
