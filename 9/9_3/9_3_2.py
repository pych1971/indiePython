import json

result = []
price = 0
first_name = ''
last_name = ''
with open('manager_sales.json') as managers:
    man = json.load(managers)
    for i in man:
        s = 0
        for j in i['cars']:
            s += j['price']
        if s > price:
            first_name = i['manager']['first_name']
            last_name = i['manager']['last_name']
            price = s
            s = price
print(first_name, last_name, price)
