a=input()
b=input()
if a[-1].upper()=='Ь':
    if a[-2].upper()==b[0].upper():
        print('Good')
    else:
        print('Bad')
else:
    if a[-1].upper()==b[0].upper():
        print('Good')
    else:
        print('Bad')
