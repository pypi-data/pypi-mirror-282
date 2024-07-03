# ONNX MTCNN

## Description
This project implements the MTCNN (Multi-task Cascaded Convolutional Networks) algorithm using ONNX (Open Neural Network Exchange) format. MTCNN is a popular face detection algorithm that consists of three stages: face detection, bounding box regression, and facial landmark localization. By using ONNX, we can leverage the benefits of interoperability and portability across different deep learning frameworks.

When you are going to use MTCNN to satisfy your face detection needs in your production environment, you can use this to get rid of the heavy Pytorch or Tensorflow dependency and instead opt for the lightweight ONNXruntime

## Features
- Face detection using MTCNN algorithm
- Bounding box regression for accurate face localization
- Facial landmark localization for detailed facial analysis

## Installation
1. Install the required dependencies: `pip install MTCNN_ONNX`

## Usage
```py
from mtcnn_onnx_simple import get_aligned_faces

image_path = "Image Path Here"
boxes, faces = get_aligned_faces(image_path)
# faces is an array of PIL Image Instances
for face in faces:
    face.show()
```


## License
This project is licensed under the [MIT License](LICENSE).
