n = input()
count = [0] * 10
for i in range(len(n)):
    count[int(n[i])] += 1
for i in range(len(count)):
    if count[i] > 0:
        print(i, count[i])
