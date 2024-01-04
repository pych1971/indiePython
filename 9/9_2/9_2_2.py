x = []
s = set()
w = ''
with open('lorem.txt') as f:
    x = f.readlines()
    for i in range(len(x)):
        x[i] = x[i].split()
        for j in range(len(x[i])):
            s.add(x[i][j].lower())
print(len(s))
