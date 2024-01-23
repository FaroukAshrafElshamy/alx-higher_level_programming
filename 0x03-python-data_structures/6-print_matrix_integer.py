#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for k in matrix[i]:
            print("{}".format(k), end='')
        print()
