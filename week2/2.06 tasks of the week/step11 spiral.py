def matrix_to_str(matrix):
    s = ''
    for row in matrix:
        for elem in row:
            s += (str(elem) + ' ')
        s += "\n"

    return s


def get_spiral_matrix(n):
    x, y, dx, dy, m = 0, 0, 0, 1, [[0] * n for _ in range(n)]
    for i in range(n * n):
        m[x][y] = str(i + 1)
        if x + dx >= n or x + dx < 0 or y + dy >= n or y + dy < 0 or m[x + dx][y + dy]:
            dx, dy = dy, -dx
        x, y = x + dx, y + dy

    return m


print(matrix_to_str(get_spiral_matrix(int(input()))))
