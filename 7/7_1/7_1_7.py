def check_password(p):
    c = 0
    z = 0
    s = 0
    for i in range(len(p)):
        if '0' <= p[i] <= '9':
            c += 1
        elif 'A' <= p[i] <= 'Z':
            z += 1
        elif p[i] in "!@#$%*":
            s += 1
    if c >= 3 and z > 0 and s > 0 and len(p) >= 10:
        print('Perfect password')
    else:
        print('Easy peasy')
