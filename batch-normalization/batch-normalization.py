import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    x = np.asarray(x)
    axis = 0
    if len(x.shape) > 2:
        gamma = np.asarray(gamma).reshape(1, -1, 1, 1)
        beta = np.asarray(beta).reshape(1, -1, 1, 1)
        axis = (0, 2, 3)
    
    mean_b = np.mean(x, axis=axis, keepdims=True)
    var_b = np.var(x, axis=axis, keepdims=True)
    X_norm = (x - mean_b) / np.sqrt(var_b + eps)
    return X_norm * gamma + beta
    