import numpy as np

def get_med(lst):
    n = len(lst)
    if n == 0:
        return 0.0
    
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2.0


def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    if len(values) == 0:
        return []

    values = np.asarray(values, dtype=np.float64)
    values_sorted = np.sort(values)

    n = len(values)
    Q2 = get_med(values_sorted)

    # Split for quartiles
    if n % 2 == 1:
        lower = values_sorted[:n//2]
        upper = values_sorted[n//2+1:]
    else:
        lower = values_sorted[:n//2]
        upper = values_sorted[n//2:]

    Q1 = get_med(lower)
    Q3 = get_med(upper)

    IQR = Q3 - Q1

    if IQR == 0:
        return [0.0] * n

    return ((values - Q2) / IQR).tolist()