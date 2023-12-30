def list_sum_recursive(a):
    if len(a) > 1:
        a[-2] += a[-1]
        a.pop(-1)
        list_sum_recursive(a)
    return a[0]
