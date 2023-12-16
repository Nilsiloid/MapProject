def calculate_iou(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    # Calculate the intersection area
    intersection_x = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    intersection_y = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    intersection_area = intersection_x * intersection_y

    # Calculate the union area
    union_area = w1 * h1 + w2 * h2 - intersection_area

    # Calculate IoU
    iou = intersection_area / union_area if union_area > 0 else 0

    return iou


def iou(pred_bbox, gt_bbox):
    """
    Calculates the Intersection over Union (IoU) between two bounding boxes.

    Args:
        pred_bbox (np.ndarray): Predicted bounding box in format [x_min, y_min, x_max, y_max]
        gt_bbox (np.ndarray): Ground truth bounding box in format [x_min, y_min, x_max, y_max]

    Returns:
        float: IoU value
    """

    # Get the intersection coordinates
    inter_x1 = max(pred_bbox[0], gt_bbox[0])
    inter_y1 = max(pred_bbox[1], gt_bbox[1])
    inter_x2 = min(pred_bbox[2], gt_bbox[2])
    inter_y2 = min(pred_bbox[3], gt_bbox[3])

    # Calculate the intersection area
    inter_w = inter_x2 - inter_x1
    inter_h = inter_y2 - inter_y1
    inter = inter_w * inter_h

    # Calculate the union area
    pred_area = (pred_bbox[2] - pred_bbox[0]) * (pred_bbox[3] - pred_bbox[1])
    gt_area = (gt_bbox[2] - gt_bbox[0]) * (gt_bbox[3] - gt_bbox[1])
    union = pred_area + gt_area - inter

    # Calculate the IoU
    iou = inter / union

    return iou

with open('predictions_bounding_boxes/sorted_label1.txt', 'r') as file1:
    lines1 = file1.readlines()

with open('test_data_bounding_boxes/box1.txt', 'r') as file2:
    lines2 = file2.readlines()


for line in lines1:
    elements = line.split()
    for lin in lines2:
        ele = lin.split()
        if(ele[0]==elements[0]):
            box1 = (int(elements[2]), int(elements[3]), int(elements[4]), int(elements[5]))
            box2 = (int(ele[2]), int(ele[3]), int(ele[4]), int(ele[5]))

            iou = calculate_iou(box1, box2)
            # iou = iou(box1, box2)
            print(ele[0] + " " + str(iou*100))

# # Example usage:
# x1,y1,w1,h1 = (191, 18, 292, 32)
# x3,y3,w2,h2 = (193, 16, 284, 25)

# x2 = x1 + w1//2
# y2 = y1 + h1//2
# x1 = x1 - w1//2
# y1 = y1 - h1//2

# x4 = x3 + w2//2
# y4 = y3 + h2//2
# x3 = x3 - w2//2
# y3 = y3 - h2//2

# box1 = (x1, y1, x2, y2)  # Example coordinates (x, y, width, height) for box 1
# box2 = (x3, y3, x4, y4)  # Example coordinates (x, y, width, height) for box 2

# # iou = iou(box1, box2)
# iou = calculate_iou(box1, box2)
# print(f"IoU: {iou}")
