def print_from(n: int) -> None:
    if n > 0:
        print(n)
        print_from(n - 1)
