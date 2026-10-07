import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    xi = np.array(x);
    pi = np.array(p);
    sum = 0.0
    for i in range(len(x)):
        sum = sum + (xi[i]*pi[i]);


    return sum
        