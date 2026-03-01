import math
import numpy as np
def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    X = np.asarray(X)
    H, W = X.shape
    H_out, W_out = math.ceil((H - pool_size) / stride) + 1, \
            math.ceil((W - pool_size) / stride) + 1


    X_pooled = np.zeros((H_out, W_out))
    for i in range(H_out):
        h_start = i * stride
        h_end = h_start + pool_size
        for j in range(W_out):
            w_start = j * stride
            w_end = w_start + pool_size
            X_pooled[i][j] = np.max(X[h_start:h_end, w_start:w_end])

    return X_pooled.tolist()