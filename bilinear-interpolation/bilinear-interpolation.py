import numpy as np
def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    # Write code here
    image = np.asarray(image, dtype = np.float64)
    H, W = image.shape

    src_y = np.zeros(new_h) if new_h == 1 else \
        np.linspace(0, H-1, new_h)
    src_x = np.zeros(new_w) if new_w == 1 else\
        np.linspace(0, W-1, new_w)

    y0 = np.floor(src_y).astype(int)
    x0 = np.floor(src_x).astype(int)

    y1 = np.clip(y0 + 1, 0, H-1)
    x1 = np.clip(x0 + 1, 0, W-1)
    
    dy = src_y - y0
    dx = src_x - x0

    y0 = y0[:, None]
    y1 = y1[:, None]
    dy = dy[:, None]

    x0 = x0[None, :]
    x1 = x1[None, :]
    dx = dx[None, :]

    Ia = image[y0, x0]
    Ib = image[y0, x1]
    Ic = image[y1, x0]
    Id = image[y1, x1]
    top = Ia * (1 - dx) + Ib * dx
    bottom = Ic * (1-dx) + Id * dx
    image_out = top * (1-dy) + bottom * dy
    return image_out.tolist()
    