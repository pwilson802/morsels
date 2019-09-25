def add(matrix1, matrix2):
    for matrix_num, matrix in enumerate(matrix2):
        for i, e in enumerate(matrix):
            matrix1[matrix_num][i] += e
    return matrix1
     

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
first = add(matrix1, matrix2)
assert (first == [[3, -3], [-3, 3]]), 'first try failed'


matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
second = add(matrix1, matrix2)
assert (second == [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]), 'second try failed'