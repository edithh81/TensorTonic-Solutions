import math
import numpy as np

def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    # Write code here
    image = np.asarray(image)
    kernel = np.asarray(kernel)
    
    H, W = image.shape
    H_k, W_k = kernel.shape

    if padding > 0:
        # pad row first
        pad_row = np.zeros((padding, W))
        image = np.vstack([pad_row, image, pad_row])
        # then pad col
        H_padded = image.shape[0]
        pad_col = np.zeros((H_padded, padding))
        image = np.hstack([pad_col, image, pad_col])
        
    H_out, W_out = math.floor((H + 2 * padding - H_k)/stride) + 1, math.floor((W + 2 * padding -  W_k)/stride) + 1
    image_out = np.zeros((H_out, W_out))

    for i in range(H_out):
        for j in range(W_out):
            # get the window first
            h_start = i * stride
            h_end = h_start + H_k
            w_start = j * stride
            w_end = w_start + W_k
            window = image[h_start:h_end, w_start:w_end]
            image_out[i,j] = np.sum(kernel * window)

    return image_out.tolist()
    
    