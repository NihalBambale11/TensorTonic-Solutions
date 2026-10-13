import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here

    arr = np.asarray(x,dtype=float)

    res = np.tanh(arr);

    return res