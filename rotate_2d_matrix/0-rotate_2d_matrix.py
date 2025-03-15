#!/usr/bin/python3
""" Module that contains a function that rotates a matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ Function that rotates a matrix 90 degrees clockwise
    """

    # create a replica of the original matrix
    copy = matrix[:]

    for i in range(len(matrix)):

        # extract the i column from the copy
        col_i = [row[i] for row in copy]

        # place it on the original matrix in reverse order
        matrix[i] = col_i[::-1]
