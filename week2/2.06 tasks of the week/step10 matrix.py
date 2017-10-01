def input_matrix(stop_word):
    matrix = []
    while True:
        row = input()
        if row == stop_word:
            break
        matrix.append([int(x) for x in row.split()])

    return matrix


def matrix_to_str(matrix):
    s = ''
    for row in matrix:
        for elem in row:
            s += (str(elem) + ' ')
        s += "\n"

    return s


def get_summed_matrix(matrix):
    final_matrix = []
    for i in range(len(matrix)):
        final_row = []
        for j in range(len(matrix[0])):
            item = matrix[i][j - 1]\
                + matrix[i - 1][j]\
                + matrix[i + 1 - len(matrix)][j]\
                + matrix[i][j + 1 - len(matrix[0])]
            final_row.append(item)
        final_matrix.append(final_row)

    return final_matrix


print(matrix_to_str(get_summed_matrix(input_matrix('end'))))
