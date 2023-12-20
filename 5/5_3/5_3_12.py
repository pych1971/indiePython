s=input()
stack=[]
psp='YES'
for i in s:
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        if not stack:
            psp='NO'
            break
        x=stack.pop()
        if x=='(' and i==')':
            continue
        if x=='{' and i=='}':
            continue
        if x=='[' and i==']':
            continue
        psp='NO'
        break
if psp=='YES' and len(stack)==0:
    print('YES')
else:
    print('NO')
