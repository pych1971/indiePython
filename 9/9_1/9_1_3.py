def create_file_with_numbers(n: int) -> None:
    f = open(f'range_{n}.txt', 'a', encoding='utf-8')
    for i in range(1, n + 1):
        f.write(str(i) + '\n')
    f.close()
