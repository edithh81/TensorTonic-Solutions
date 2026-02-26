import numpy as np
import math

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pe_mat = np.zeros((seq_len, d_model))
    
    pos = np.arange(seq_len)[:, np.newaxis] # (seq_len, 1)
    i = np.arange(0, math.ceil(d_model/2) )
    demonitor = base ** (2 * i / d_model)
    
    
    pe_mat[:, 0::2] =  np.sin(pos / demonitor)
    pe_mat[:, 1::2] = np.cos(pos / demonitor[:pe_mat[:, 1::2].shape[1]])
    return pe_mat
    