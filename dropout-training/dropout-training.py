import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    x = np.asarray(x)
    if rng is None:
        rng = np.random.default_rng()

    if p == 0.0:
        return x.astype(float), np.ones(x.shape)

    shape_ = x.shape
    dropout_pattern = (rng.random(shape_) < (1 - p)).astype(float)
    dropout_pattern /= (1 - p)
    out = x * dropout_pattern
    return out, dropout_pattern