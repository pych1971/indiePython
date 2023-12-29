def first_unique_char(s):
    dic = {}
    x = -1
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    for i in range(len(s)):
        if dic[s[i]] == 1:
            x = i
            break
    return x


s = input()
print(first_unique_char(s))
