phrase = 'Take only the words that start with t in this sentence'
a = phrase.split()
b = [a[i] for i in range(len(a)) if a[i][0].lower() == 't']
print(b)
