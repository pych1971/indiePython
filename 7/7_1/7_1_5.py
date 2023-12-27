def sum_num(a):
    s = 0
    for i in range(len(a)):
        if '0' <= a[i] <= '9':
            s += int(a[i])
    print(s)
