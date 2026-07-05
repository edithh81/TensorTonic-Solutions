import math
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # total anchors = H_feat \times W_feat \times |scales| \times |ratios|
    stride = image_size / feature_size

    anchors = []
    # num cell
    for i in range(feature_size):
        for j in range(feature_size):
            c_x = (j + 0.5 ) * stride
            c_y = (i + 0.5 ) * stride
            for s in scales:
                for r in aspect_ratios:
                    w = s * math.sqrt(r)
                    h = s / math.sqrt(r)
                    x_1 = c_x - w/2
                    y_1 = c_y - h/2
                    x_2 = c_x + w/2
                    y_2 = c_y + h/2
                    anchors.append([x_1, y_1, x_2, y_2])

    return anchors
                    