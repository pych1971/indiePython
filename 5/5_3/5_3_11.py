a=input()
aOpen=0
aClose=0
for i in range(len(a)):
    if a[i]=="(":
        aOpen+=1
    else:
        aClose+=1
    if aClose>aOpen:
        print('NO')
        break
if aClose==aOpen:
    print('YES')
elif aOpen>aClose:
    print('NO')
