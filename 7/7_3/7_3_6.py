def find_duplicate(lst):
    lst_ch = []
    lst_dic = {}
    for i in range(len(lst)):
        if lst[i] in lst_dic:
            lst_dic[lst[i]] += 1
        else:
            lst_dic[lst[i]] = 1
    for i in range(len(lst)):
        if lst[i] not in lst_ch and lst_dic[lst[i]] > 1:
            lst_ch.append(lst[i])
    return (lst_ch)


assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
print('Все успешно')
