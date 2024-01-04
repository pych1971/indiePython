def file_read(file_name: str) -> None:
    f = open(file_name, encoding='utf-8')
    print(f.read())
