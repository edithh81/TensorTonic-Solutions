import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    anchor, positive, negative = np.array(anchor), np.array(positive), np.array(negative)

    if anchor.ndim == 1:
        anchor = anchor[None, :]
        positive = positive[None, :]
        negative = negative[None, :]
        
    dist_ap = np.linalg.norm(anchor - positive, axis = 1)
    dist_an = np.linalg.norm(anchor - negative, axis = 1)
    loss = np.maximum(0, dist_ap**2 - dist_an**2 + margin)

    return np.mean(loss)