m1 = [
    [1,   2], 
    [30, 40]
]
m2 = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # [0,0] + [1,1] + [2,2]
    n = len(matrix)
    diag_sum = 0
    for i in range(n):
        diag_sum += matrix[i][i]
        # print(diag_sum)
        diag_sum += matrix[i][-1-i]
        # print(diag_sum)
    return diag_sum


print(sum_up_diagonals(m1))
print(sum_up_diagonals(m2))