def file_n_lines(file_name: str, n: int) -> None:
    f = open(file_name, encoding='utf-8')
    for i in range(n):
        print(f.readline().strip())
