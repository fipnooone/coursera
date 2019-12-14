from sys import stdin
from copy import deepcopy
import numpy as np


class MatrixError(BaseException):
    def __init__(self, other1, other):
        self.matrix1 = Matrix(other1)
        self.matrix2 = Matrix(other)


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) \
                != len(other.matrix[0]):
            raise MatrixError(self.matrix, other.matrix)
        else:
            return Matrix(list(map(
                lambda x, y: list(map(lambda z, w: z + w, x, y)),
                self.matrix, other.matrix)))

    def __mul__(self, other):
        if isinstance(other, list):
            return Matrix(np.ndarray(self.matrix) * np.ndarray(other))
        else:
            return Matrix([[i * other for i in list] for list in self.matrix])

    def transpose(self):
        self.matrix = list(zip(*self.matrix))
        return Matrix(self.matrix)

    def transposed(self):
        return Matrix(list(zip(*self.matrix)))

    __rmul__ = __mul__


exec(stdin.read())
