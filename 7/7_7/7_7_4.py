def only_one_positive(*args):
    s = 0
    for i in args:
        if i > 0:
            s += 1
    if s == 1:
        return True
    else:
        return False
