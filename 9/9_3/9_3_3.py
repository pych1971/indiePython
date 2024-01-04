import json

summa = 0
id = 0
n = 0
with open('group_people.json') as group:
    group = json.load(group)
    for i in group:
        n = 0
        for j in i['people']:
            if j['gender'] == 'Female' and j['year'] > 1977:
                n += 1
        if n > summa:
            summa = n
            n = summa
            id = i['id_group']
print(id, summa)
