import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here

    vw_dot = np.dot(v,w)
    v_norm = np.linalg.norm(v)
    w_norm = np.linalg.norm(w)

    eps = 1e-10
    if v_norm * w_norm < eps:
        return np.nan
    return np.arccos(np.clip(vw_dot / (v_norm * w_norm), -1, 1))
    