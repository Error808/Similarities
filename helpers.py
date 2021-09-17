from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""
    w = len(b) + 1
    h = len(a) + 1

    # creating the matrix, first creates width then height
    matrix = [[0 for x in range(w)] for y in range(h)]
    matrix[0][0] = (0, None)

    # Base case
    # width
    for i in range(1, w):
        matrix[0][i] = (i, Operation.INSERTED)
    # height
    for i in range(1, h):
        matrix[i][0] = (i, Operation.DELETED)

    # table filling
    for i in range(1, h):
        for j in range(1, w):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1

            c = min(matrix[i][j - 1][0] + 1,      # inserted, left of the box
                    matrix[i - 1][j][0] + 1,      # deleted, above the box
                    matrix[i - 1][j - 1][0] + cost)  # substitution, diagnal of the box

            if (c == matrix[i][j - 1][0] + 1):
                matrix[i][j] = (c, Operation.INSERTED)
            elif (c == matrix[i - 1][j][0] + 1):
                matrix[i][j] = (c, Operation.DELETED)
            else:
                matrix[i][j] = (c, Operation.SUBSTITUTED)

    return matrix
