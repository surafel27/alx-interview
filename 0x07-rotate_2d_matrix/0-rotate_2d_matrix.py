#!/usr/bin/python3
'''rotate 2D matrix on clockwise 90 degree'''


def rotate_2d_matrix(matrix):
    '''n x n 2D matrix, rotate it 90 degrees clockwise'''
    num_matrix = len(matrix)
    for row in range(num_matrix):
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row], \
                    matrix[row][col]
    for row in matrix:
        row.reverse()
