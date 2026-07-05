import numpy as np

def get_norm(matrix, norm_type="l2", axis=None):
    if norm_type == "l2":
        return np.sqrt(np.sum(matrix ** 2, axis=axis, keepdims=True))
    elif norm_type == "l1":
        return np.sum(np.abs(matrix), axis=axis, keepdims=True)
    elif norm_type == "max":
        return np.max(np.abs(matrix), axis=axis, keepdims=True)
    else:
        return None


def matrix_normalization(matrix, axis=None, norm_type="l2"):
    matrix = np.asarray(matrix, dtype=float)
    shape_ = matrix.shape
    # Only accept 2D matrices
    if matrix.ndim != 2:
        return None

    # Validate axis
    if axis is not None and (axis < 0 or axis >= matrix.ndim):
        return None
    denominator = get_norm(matrix, norm_type=norm_type, axis=axis)
    if denominator is None:
        return None
    # prevent division by zero
    denominator = np.where(denominator == 0, 1, denominator)
    return matrix / denominator