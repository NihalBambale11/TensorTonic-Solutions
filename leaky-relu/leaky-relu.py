import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Convert input to a NumPy array to handle scalars, lists, and arrays uniformly
    x_arr = np.asarray(x, dtype=float)
    
    # Apply x if x >= 0, otherwise apply alpha * x element-wise
    return np.where(x_arr >= 0, x_arr, alpha * x_arr)


# BRUTE FORCE
# import numpy as np

# def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
#     """
#     Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
#     """
#     # Write code here

#     arr = np.array(x)
#     res = []
#     for i in range(len(arr)):
#         if arr[i] <= 0:
#             res.append(arr[i] * alpha)
#         else:
#             res.append(arr[i])
            
#     return np.array(res)