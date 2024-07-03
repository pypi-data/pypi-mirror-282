import numpy as np
from PIL import Image

def preprocess(img):
    """Arguments:
        img: an instance of PIL.Image.
       Returns:
        a float numpy array of shape (1, c, H, W), where H and W are the height and width of the image.
    """
    img = img.transpose((2, 0, 1))
    img = np.expand_dims(img, axis=0)
    img = (img - 127.5)*0.0078125
    return img

def nms(boxes, overlap_threshold, mode="union"):
    """
    Arguments:
        boxes: a float numpy array of shape (n_boxes, 5).
        overlap_threshold: a float number.
        mode: either "union" or "min".
    
    Returns:
        list with indices of the selected boxes
    """

    if len(boxes) == 0:
        return []
    
    pick = []

    x1, y1, x2, y2, score = [boxes[:, i] for i in range(5)]

    area = (x2 - x1 + 1.0) * (y2 - y1 + 1.0)
    ids = np.argsort(score)

    while len(ids) > 0:

        last = len(ids) - 1
        i = ids[last]
        pick.append(i)

        ix1 = np.maximum(x1[i], x1[ids[:last]])
        iy1 = np.maximum(y1[i], y1[ids[:last]])

        ix2 = np.minimum(x2[i], x2[ids[:last]])
        iy2 = np.minimum(y2[i], y2[ids[:last]])

        w = np.maximum(0.0, ix2 - ix1 + 1.0)
        h = np.maximum(0.0, iy2 - iy1 + 1.0)

        inter = w * h
        if mode == "min":
            o = inter / np.minimum(area[i], area[ids[:last]])
        elif mode == "union":
            o = inter / (area[i] + area[ids[:last]] - inter)
        
        ids = np.delete(ids, np.concatenate(([last], np.where(o > overlap_threshold)[0])))
    
    return pick

def calibrate_box(bboxes, offsets):
    """
    Arguments:
        bboxes: a float numpy array of shape (n_boxes, 5).
        offsets: a float numpy array of shape (n_boxes, 4).
    
    Returns:
        a float numpy array of shape (n_boxes, 5).   
    """

    x1, y1, x2, y2 = [bboxes[:, i] for i in range(4)]
    w = x2 - x1 + 1.0
    h = y2 - y1 + 1.0
    w = np.expand_dims(w, axis=1)
    h = np.expand_dims(h, axis=1)

    translation = np.hstack([w, h, w, h]) * offsets
    bboxes[:, :4] = bboxes[:, :4] + translation
    return bboxes

def convert_to_square(bboxes):
    """
    Arguments:
        bboxes: a float numpy array of shape (n_boxes, 5).
    
    Returns:
        a float numpy array of shape (n_boxes, 5).   
    """
    square_bboxes = np.zeros_like(bboxes)
    x1, y1, x2, y2 = [bboxes[:, i] for i in range(4)]
    w = x2 - x1 + 1.0
    h = y2 - y1 + 1.0
    max_side = np.maximum(w, h)
    square_bboxes[:, 0] = x1 + w * 0.5 - max_side * 0.5
    square_bboxes[:, 1] = y1 + h * 0.5 - max_side * 0.5
    square_bboxes[:, 2] = square_bboxes[:, 0] + max_side - 1.0
    square_bboxes[:, 3] = square_bboxes[:, 1] + max_side - 1.0
    return square_bboxes

def correct_bboxes(bboxes, width, height):
    """
     Arguments:
        bboxes: a float numpy array of shape [n, 5],
            where each row is (xmin, ymin, xmax, ymax, score).
        width: a float number.
        height: a float number.

    Returns:
        dy, dx, edy, edx: a int numpy arrays of shape [n],
            coordinates of the boxes with respect to the cutouts.
        y, x, ey, ex: a int numpy arrays of shape [n],
            corrected ymin, xmin, ymax, xmax.
        h, w: a int numpy arrays of shape [n],
            just heights and widths of boxes.

        in the following order:
            [dy, edy, dx, edx, y, ey, x, ex, w, h].
    """

    x1, y1, x2, y2 = [bboxes[:, i] for i in range(4)]
    w, h = x2 - x1 + 1.0, y2 - y1 + 1.0
    num_boxes = bboxes.shape[0]

    x, y, ex, ey = x1, y1, x2, y2

    dx, dy = np.zeros(num_boxes), np.zeros(num_boxes)
    edx, edy = w.copy() - 1.0, h.copy() - 1.0

    ind = np.where(ex > width - 1.0)[0]
    edx[ind] = w[ind] + width - 2.0 - ex[ind]
    ex[ind] = width - 1.0

    ind = np.where(ey > height - 1.0)[0]
    edy[ind] = h[ind] + height - 2.0 - ey[ind]
    ey[ind] = height - 1.0

    ind = np.where(x < 0.0)[0]
    dx[ind] = 0.0 - x[ind]
    x[ind] = 0.0

    ind = np.where(y < 0.0)[0]
    dy[ind] = 0.0 - y[ind]
    y[ind] = 0.0

    return_list = [dy, edy, dx, edx, y, ey, x, ex, w, h]
    return_list = [item.astype(np.int32) for item in return_list]

    return return_list

def get_image_boxes(bboxes, img, size=24):

    num_boxes = len(bboxes)
    width, height = img.size

    [dy, edy, dx, edx, y, ey, x, ex, tmpw, tmph] = correct_bboxes(bboxes, width, height)
    img_boxes = np.zeros((num_boxes, 3, size, size), dtype=np.float32)

    for i in range(num_boxes):
        img_box = np.zeros((tmph[i], tmpw[i], 3), 'uint8')

        img_array = np.asarray(img, 'uint8')
        img_box[dy[i]:(edy[i] + 1), dx[i]:(edx[i] + 1), :] = img_array[y[i]:(ey[i] + 1), x[i]:(ex[i] + 1), :]

        img_box = Image.fromarray(img_box)
        img_box = img_box.resize((size, size), Image.BILINEAR)
        img_box = np.asarray(img_box, 'float32')
        
        img_boxes[i, :, :, :] = preprocess(img_box)
    
    return img_boxes

