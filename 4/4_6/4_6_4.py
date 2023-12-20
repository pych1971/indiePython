a=input()
while len(a)!=0:
    if a[0]=='e' or a[0]=='a':
        print('Ага! Нашлась')
        break
    print(f'Текущая буква: {a[0]}')
    a=a[1:]
    if len(a)==0:
        print('Распечатали все буквы')
