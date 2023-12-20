a=int(input())
p=1
while a>0:
    p*=a%10
    a=a//10
print(p)
