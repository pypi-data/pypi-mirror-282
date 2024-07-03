import math
from PIL import Image
import numpy as np

from helpers import preprocess, nms

def first_stage(image, pnet, scale, threshold):
    width, height = image.size
    sw, sh = math.ceil(width * scale), math.ceil(height * scale)
    img = image.resize((sw, sh), Image.BILINEAR)
    img = np.array(img, dtype=np.float32)

    img = preprocess(img)
    
    output = pnet.run(None, {"l_x_": img})
    
    probs = output[1][0, 1, :, :]
    offsets = output[0]

    boxes = generate_bboxes(probs, offsets, scale, threshold)
    if len(boxes) == 0:
        return None
    
    keep = nms(boxes[:, :5], overlap_threshold=0.5)
    return boxes[keep]

def generate_bboxes(probs, offsets, scale, threshold):
    """
    Arguments:
        probs: a float numpy array of shape (H, W).
        offsets: a float numpy array of shape (1, 4, H, W).
        scale: a float number.
        threshold: a float number.
    
    Returns:
        a float numpy array of shape (n_boxes, 9).
    """

    stride = 2
    cell_size = 12

    inds = np.where(probs > threshold)
    if inds[0].size == 0:
        return np.array([])
    
    tx1, ty1, tx2, ty2 = [offsets[0, i, inds[0], inds[1]] for i in range(4)]

    offsets = np.array([tx1, ty1, tx2, ty2])
    score = probs[inds[0], inds[1]]

    bounding_boxes = np.vstack([
        np.round((stride * inds[1] + 1) / scale),
        np.round((stride * inds[0] + 1) / scale),
        np.round((stride * inds[1] + 1 + cell_size) / scale),
        np.round((stride * inds[0] + 1 + cell_size) / scale),
        score,
        offsets
    ])

    return bounding_boxes.T