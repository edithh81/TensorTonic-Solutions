import math
import numpy as np

def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here
    if angle_degrees == 0:
        return image
    angle_degrees = math.radians(angle_degrees)
    image = np.asarray(image)
    H, W = image.shape
    image_rotated = np.zeros((H, W))
    cy, cx = (H-1)/2, (W-1)/2
    for i in range(H):
        for j in range(W):
            dy = i - cy
            dx = j - cx
            src_y = round(cy + dy * math.cos(angle_degrees) + dx * math.sin(angle_degrees))
            src_x = round(cx - dy * math.sin(angle_degrees) + dx * math.cos(angle_degrees))
            if src_y >= W or src_y < 0 or src_x < 0 or src_x >= H:
                image_rotated[i][j] = 0
            else:
                image_rotated[i][j] = image[src_y][src_x]

    return image_rotated.tolist()
        