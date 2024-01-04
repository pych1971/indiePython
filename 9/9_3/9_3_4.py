import json

result = []
with open('Alphabet.json') as alphabet:
    alpha = json.load(alphabet)
    with open('Abracadabra__1_.txt') as abracadabra:
        abra = abracadabra.readlines()
    with open('result.txt', 'w') as result:
        for i in range(len(abra)):
            for j in range(len(abra[i])):
                if 'A' <= abra[i][j] <= 'z':
                    result.write(alpha[abra[i][j]])
                else:
                    result.write(abra[i][j])
