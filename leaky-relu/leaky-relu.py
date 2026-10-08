import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here

    arr = np.array(x)
    res = []
    for i in range(len(arr)):
        if arr[i] <= 0:
            res.append(arr[i] * alpha)
        else:
            res.append(arr[i])
            
    return np.array(res)