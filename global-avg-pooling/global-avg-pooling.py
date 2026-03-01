import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code 
    if len(x.shape) < 3:
        raise ValueError
    x = np.asarray(x, dtype = np.float64)
    
    H,W = x.shape[-2:]

    avg_over_h_w = np.sum(x, axis = (-2, -1))
    return avg_over_h_w / (H*W)