x = []
words = dict()
with open('lorem.txt') as f:
    x = f.readlines()
    for i in range(len(x)):
        x[i] = x[i].split()
        for j in range(len(x[i])):
            a = x[i][j].upper()
            if a in words.keys():
                words[a] += 1
            else:
                words[a] = 1
