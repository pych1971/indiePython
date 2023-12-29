def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
    a = []
    for i in range(size):
        a.append([0] * size)
    for i in range(size):
        for j in range(size):
            if i == j:
                a[i][j] = i + 1
            elif j > i:
                a[i][j] = up_fill
            elif j < i:
                a[i][j] = down_fill
    return a
