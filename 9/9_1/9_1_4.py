from string import punctuation


def longest_word_in_file(file_name: str) -> str:
    s = []
    l = 0
    w = ''
    f = open(file_name, encoding='utf-8')
    s = f.readlines()
    for i in range(len(s)):
        s[i] = s[i].split()
        for j in range(len(s[i])):
            if (len(s[i][j].strip(punctuation))) >= l:
                l = len(s[i][j].strip(punctuation))
                w = s[i][j].strip(punctuation)
    f.close()
    return w
