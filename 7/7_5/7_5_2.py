def get_word_indices(strings: list[str]) -> dict:
    a = {}
    x = ''
    for i in range(len(strings)):
        for j in range(len(x := strings[i].lower().split())):
            if x[j] in a:
                a[x[j]] += [i]
            else:
                a[x[j]] = [i]
    return a
