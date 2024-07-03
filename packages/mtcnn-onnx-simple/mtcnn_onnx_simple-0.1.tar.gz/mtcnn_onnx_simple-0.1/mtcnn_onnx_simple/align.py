import sys
import os

import src.mtcnn as mtcnn
from PIL import Image

mtcnn_model = mtcnn.MTCNN(crop_size=(112,112))

def get_aligned_faces(image_path,rgb_pil_image=None):
    if rgb_pil_image is None:
        img = Image.open(image_path).convert("RGB")
    else:
        assert isinstance(rgb_pil_image,Image.Image)
        img = rgb_pil_image
    
    try:
        bboxes, faces = mtcnn_model.align_multi(img)
    except Exception as e:
        print(f"Error in align_multi: {e}")
        return None
    
    return bboxes,faces