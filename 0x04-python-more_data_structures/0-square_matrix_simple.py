#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for x in range(len(matrix)):
        new_matrix[x] = list(map(lambda i: i**2, matrix[x]))

    return (new_matrix)
