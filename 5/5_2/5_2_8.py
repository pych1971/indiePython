n=int(input())
s=0
for i in range(1,n):
    if i%3==0 or i%5==0:
#        print(i)
        s+=i
print(s)
