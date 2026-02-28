import numpy as np
def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    # Write code here
    image = np.asarray(image)
    H, W = image.shape
    image_out = np.zeros((new_h, new_w))
    
    h_scale = (H-1) / (new_h-1) if new_h != 1 else 0
    w_scale = (W-1) / (new_w -1) if new_w != 1 else 0
    
    for i in range(new_h):
        src_y = i * h_scale
        y0 = int(np.floor(src_y))
        y1 = min(y0 + 1, H-1)
        dy = src_y - y0
        for j in range(new_w):
            src_x = j * w_scale
            x0 = int(np.floor(src_x))
            x1 = min(x0+1, W-1)
            dx = src_x - x0
            top = image[y0][x0] * (1-dx) + image[y0][x1] * dx
            bottom = image[y1][x0] * (1-dx) + image[y1][x1] * dx
            res = top * (1-dy) + bottom * dy
            image_out[i][j] = res
        
    return image_out.astype(np.float32).tolist()
            
            