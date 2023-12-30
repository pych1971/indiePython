def info_kwargs(**kwargs):
    a = sorted(kwargs.keys())
    for i in a:
        print(f'{i} = {kwargs[i]}')
