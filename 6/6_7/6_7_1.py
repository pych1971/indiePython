workers = {
    'employer1': {'name': 'Jhon', 'salary': 7500},
    'employer2': {'name': 'Emma', 'salary': 8000},
    'employer3': {'name': 'Brad', 'salary': 500}
}
people = ['employer1', 'employer2', 'employer3']
for i in people:
    if workers[i]['name'] == 'Brad':
        workers[i]['salary'] = 8500
print(workers)
