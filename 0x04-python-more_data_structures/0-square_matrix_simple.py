#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m2 = []
    for i in range(len(matrix)):
        copy = list(map((lambda x: x**2), matrix[i]))
        m2.append(copy)
    return m2
