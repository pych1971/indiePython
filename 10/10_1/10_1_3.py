week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = ((i, week[(i + 4) % 7]) for i in range(1, 78))
for i in range(1, 78):
    print(next(days))
