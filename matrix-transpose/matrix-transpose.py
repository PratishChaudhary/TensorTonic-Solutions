import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    result = []
    for i in range(len(A[0])):
        row = []
        for j in A:
            row.append(j[i])
        (result.append(row))
    return np.array(result)