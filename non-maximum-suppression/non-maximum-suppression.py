from collections import defaultdict
def calculate_iou(box_a, box_b):
    # x1, y1, x2, y2
    a_area = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    b_area = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    i_x1 = max(box_a[0], box_b[0])
    i_x2 = min(box_a[2], box_b[2])
    i_y1 = max(box_a[1], box_a[1])
    i_y2 = min(box_a[3], box_b[3])

    intersection = max(0,(i_x2 - i_x1)) * max(0, (i_y2-i_y1))

    total_area = a_area + b_area - intersection
    return intersection / total_area
def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    """
    # sort with score first
    bbox_scores = [(i,b,s) for i,(b, s) in enumerate(zip(boxes, scores))]
    bbox_scores = sorted(bbox_scores, key=lambda x: x[2], reverse=True)

    # iou scores 
    iou_scores = defaultdict(list)

    for i in range(len(bbox_scores)):
        for j in range(i + 1, len(bbox_scores)):
            iou_scores[i].append((j, calculate_iou(bbox_scores[i][1], bbox_scores[j][1])))

    # eliminate
    keep_box = [True for _ in range(len(bbox_scores))]
    for i in range(len(bbox_scores)):
        if keep_box[i] == False: 
                continue 
        for j, iou_score in iou_scores[i]:
            if iou_score >= iou_threshold:
                keep_box[j] = False

    res = []
    for i, bool_val in enumerate(keep_box):
        if bool_val:
            res.append(bbox_scores[i][0])


    return res
            
        
    