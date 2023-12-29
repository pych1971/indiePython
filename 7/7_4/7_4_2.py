def first_repeated_word(a: str) -> str:
    'Находит первый дубль в строке'
    aList = a.split()
    ret = None
    y = len(aList)
    for i in range(0, len(aList) - 1):
        for j in range(i + 1, len(aList)):
            if aList[i] == aList[j] and j < y:
                ret = aList[i]
                y = j
    return ret
