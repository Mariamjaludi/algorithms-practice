# Search In Sorted Matrix
# You are given a two-dimensional array (matrix) of distinct integers where each
# row is sorted and each column is also sorted. The matrix does not necessarily
# have the same height and width. You are also given a target number, and you
# must write a function that returns an array of the row and column indices of
# the target number if it is contained in the matrix and [-1, -1] if it is not
# contained in the matrix.

# sample input:
input = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

target = 44

output = [3, 3]

def searchInSortedMatrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1

    while i < len(matrix) and j >= 0:
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            matrix[i][j]
    return [-1, -1]
