def find_lines_len_more_6(file_name: str) -> int:
    with open(file_name) as f:
        n = len(f.readlines())
        f.seek(0)
        i = 0
        for j in range(n):
            if len(f.readline().strip()) > 6:
                i += 1
    return i
