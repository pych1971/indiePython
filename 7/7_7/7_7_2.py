def check_sum(*args):
    s = 0
    for i in args:
        s += i
    if s < 50:
        print('not enough')
    else:
        print('verification passed')
