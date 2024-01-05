def my_range_gen(*args) -> int:
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    else:
        start = args[0]
        stop = args[1]
        step = args[2]
    i = start
    if step == 0:
        return
    if step > 0:
        if start > stop:
            return
        else:
            while i < stop:
                yield i
                i += step
    if step < 0:
        if start < stop:
            return
        else:
            while i > stop:
                yield i
                i += step
