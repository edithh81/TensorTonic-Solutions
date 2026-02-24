import numpy as np
def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    X = np.asarray(X)
    H, W = X.shape
    H_out, W_out  = H // pool_size, W // pool_size
    X_pooled = np.zeros((H_out, W_out))
    for i in range(H_out):
        for j in range(W_out):
            h_start = i * pool_size
            h_end = h_start + pool_size
            w_start = j * pool_size
            w_end = w_start + pool_size
            X_pooled[i][j] = np.max(X[h_start:h_end, w_start:w_end])   

    return X_pooled.tolist()