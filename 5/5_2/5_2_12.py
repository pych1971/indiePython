N=int(input())
s=''
for i in range(N):
    a=input()
    if a.lower().find('соль')==-1:
        s=s+a+', '
print(s[:-2])
