from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    arr = np.array(x)
    
    # 1. Calculate mean and median, strictly casting to float
    mean = float(np.mean(arr))
    median = float(np.median(arr))
    
    # 2. Calculate the mode
    counts = Counter(x)
    max_freq = max(counts.values())
    
    # Get all values that share the highest frequency
    mode_candidates = [key for key, freq in counts.items() if freq == max_freq]
    
    # Tie-breaker: choose the smallest value, cast to float
    mode = float(min(mode_candidates))
    
    return {
        "mean": mean, 
        "median": median, 
        "mode": mode 
    }