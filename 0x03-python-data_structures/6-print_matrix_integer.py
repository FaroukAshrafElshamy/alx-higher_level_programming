#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for k in matrix[i]:
            if k != matrix[i][-1]:
                print("{}".format(k), end=' ')
            else:
                print("{}".format(k),end='')
        print()
