import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    orig_rows = len(A)
    orig_cols = len(A[0])
    

    ls = [[0 for _ in range(orig_rows)] for _ in range(orig_cols)]

    for i in range(len(A)):
        for j in range(len(A[0])):
            ls[j][i] = A[i][j]


    return np.array(ls);
