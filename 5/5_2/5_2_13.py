N=int(input())
s=''
for i in range(N):
    a=input()
    if len(a)>10:
        s=s+a[0]+str(len(a)-2)+a[-1]+'\n'
    else:
        s=s+a+'\n'
print(s)
