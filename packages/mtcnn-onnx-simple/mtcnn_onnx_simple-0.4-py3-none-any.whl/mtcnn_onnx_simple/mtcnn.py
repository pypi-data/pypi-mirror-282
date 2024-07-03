import numpy as np
from PIL import Image
import onnxruntime as rt
from .first_stage import first_stage
from .helpers import preprocess, nms, calibrate_box, convert_to_square, get_image_boxes
from .align_transformations import warp_and_crop_face, get_reference_facial_points

class MTCNN:
    def __init__(self, crop_size = (112, 112)):
        self.pnet = rt.InferenceSession("models/p_net.onnx")
        self.rnet = rt.InferenceSession("models/r_net.onnx")
        self.onet = rt.InferenceSession("models/o_net.onnx")
        
        assert crop_size in [(112, 112), (96,112)]
        self.crop_size = crop_size
        self.min_face_size = 20
        self.thresholds = [0.6, 0.7, 0.9]
        self.nms_thresholds = [0.7, 0.7, 0.7]
        self.factor = 0.85

        self.reference = get_reference_facial_points(default_square=crop_size[0] == crop_size[1])

    def align_multi(self, image):
        boxes, landmarks = self.detect_Faces(image, self.min_face_size, self.thresholds, self.nms_thresholds, self.factor)
        faces = []
        for landmark in landmarks:
            facial5points = [[landmark[j], landmark[j + 5]] for j in range(5)]
            warped_face = warp_and_crop_face(np.array(image), facial5points, self.reference, crop_size=self.crop_size)
            faces.append(Image.fromarray(warped_face))
        return boxes, faces
    
    def detect_Faces(self, image, min_face_size, thresholds, nms_thresholds, factor):
        """
        Arguments:
            image: an instance of PIL.Image.
            min_face_size: a float number
            thresholds: a list of length 3
            nms_thresholds: a list of length 3
        
        Returns:
            two float numpy arrays of shapes (n_boxes, 4) and (n_boxes, 10),
            where n_boxes is the number of bounding boxes.
        """
        width, height = image.size
        min_length = min(height, width)

        min_detection_size = 12
        scales = []

        m = min_detection_size / min_face_size
        min_length *= m

        factor_count = 0
        while min_length > min_detection_size:
            scales.append(m * factor ** factor_count)
            min_length *= factor
            factor_count += 1
        
        # Stage 1: P-Net
        bounding_boxes = []

        for s in scales:
            boxes = first_stage(image, self.pnet, s, thresholds[0])
            if boxes is not None:
                bounding_boxes.append(boxes)
        
        if len(bounding_boxes) == 0:
            return [], []

        bounding_boxes = np.vstack(bounding_boxes)
        keep = nms(bounding_boxes[:, 0:5], nms_thresholds[0])
        bounding_boxes = bounding_boxes[keep]

        bounding_boxes = calibrate_box(bounding_boxes[:, 0:5], bounding_boxes[:, 5:])

        bounding_boxes = convert_to_square(bounding_boxes)

        bounding_boxes[:, 0:4] = np.round(bounding_boxes[:, 0:4])
        # Stage 2: R-Net
        img_boxes = get_image_boxes(bounding_boxes, image, size=24)
        
       
        rnet_output = self.rnet.run(None, {"l_x_": img_boxes})
        
        offsets = rnet_output[0]
        probs = rnet_output[1]
       
        keep = np.where(probs[:,1] > thresholds[1])[0]
        
        bounding_boxes = bounding_boxes[keep]
        bounding_boxes[:, 4] = probs[keep, 1].reshape((-1,))
        offsets = offsets[keep]

        keep = nms(bounding_boxes, nms_thresholds[1])
        bounding_boxes = bounding_boxes[keep]
        bounding_boxes = calibrate_box(bounding_boxes, offsets[keep])
        bounding_boxes = convert_to_square(bounding_boxes)
        bounding_boxes[:, 0:4] = np.round(bounding_boxes[:, 0:4])
        #Stage 3: O-Net
        img_boxes = get_image_boxes(bounding_boxes, image, size=48)
        if len(img_boxes) == 0:
            return [], []
        
        onet_output = self.onet.run(None, {"l_x_": img_boxes})
        landmarks = onet_output[0]
        offsets = onet_output[1]
        probs = onet_output[2]

        keep = np.where(probs[:, 1] > thresholds[2])[0]
        bounding_boxes = bounding_boxes[keep]
        bounding_boxes[:, 4] = probs[keep, 1].reshape((-1,))
        offsets = offsets[keep]
        landmarks = landmarks[keep]

        width = bounding_boxes[:, 2] - bounding_boxes[:, 0] + 1.0
        height = bounding_boxes[:, 3] - bounding_boxes[:, 1] + 1.0
        xmin, ymin = bounding_boxes[:, 0], bounding_boxes[:, 1]
        landmarks[:, 0:5] = np.expand_dims(xmin, 1) + np.expand_dims(width, 1) * landmarks[:, 0:5]
        landmarks[:, 5:10] = np.expand_dims(ymin, 1) + np.expand_dims(height, 1) * landmarks[:, 5:10]

        bounding_boxes = calibrate_box(bounding_boxes, offsets)
        keep = nms(bounding_boxes, nms_thresholds[2], mode="min")
        bounding_boxes = bounding_boxes[keep]
        landmarks = landmarks[keep]

        return bounding_boxes, landmarks

        


        