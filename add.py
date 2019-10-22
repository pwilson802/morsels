from copy import deepcopy

def add(*args):
    # Check the args are valid before processing
    first_matrix_set_len = len(args[0])
    matrix_len = len(args[0][0])
    for matrix_set in args:
        if len(matrix_set) != first_matrix_set_len:
            raise ValueError
        for matrix in matrix_set:
            if len(matrix) != matrix_len:
                raise ValueError("Given matrices are not the same size.")
        
    result = deepcopy(args[0])
    for matrix_set in args[1:]:
        for matrix_num, matrix in enumerate(matrix_set):
            for i, e in enumerate(matrix):
                result[matrix_num][i] += e
    return result
     

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
first = add(matrix1, matrix2)
assert (first == [[3, -3], [-3, 3]]), 'first try failed'


matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
second = add(matrix1, matrix2)
assert (second == [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]), 'second try failed'

# matrix1 = [[1, 9], [7, 3]]
# matrix2 = [[5, -4], [3, 3]]
# matrix3 = [[2, 3], [-3]]
# third = add(matrix1, matrix2, matrix3)
# assert (third == [[8, 8], [7, 7]]), 'more than 2 matrix is failing'
