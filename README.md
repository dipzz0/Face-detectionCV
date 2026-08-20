Face Detection is a computer vision technique used to identify and locate human faces in an image or video. It is widely used in applications such as security systems, surveillance, and biometric authentication.
RetinaFace is a deep learning-based face detection model designed to accurately detect faces of different sizes, angles, and lighting conditions. Unlike traditional methods such as Haar Cascade, RetinaFace can detect multiple faces, including small, tilted, and partially occluded faces.
The model identifies each detected face by generating a bounding box around it. Its accuracy and robustness make it suitable for various real-world computer vision applications.

Software Requirements

Google Colab

Python 3.x

RetinaFace Library

OpenCV

Image containing one or more faces

Procedure (Step-by-Step)

Step 1:
Open Google Colab.

Step 2:
Install the RetinaFace library and import the required libraries.

Step 3:
Upload an image containing one or more faces.

Step 4:
Read the uploaded image using OpenCV.

Step 5:
Detect all faces using the RetinaFace model.

Step 6:
Draw a bounding box around each detected face.

Step 7:
Display the output image with the detected faces.

Example

Input Image:

Upload an image containing one or more faces.

<img width="696" height="390" alt="image" src="https://github.com/user-attachments/assets/06e9ca5b-271e-4828-bd78-8089bc9f5f50" />


Output Image:

The RetinaFace model detects the faces and draws bounding boxes around them.

<img width="702" height="394" alt="image" src="https://github.com/user-attachments/assets/d5742f37-fe03-405a-82d6-eeecbfbb8019" />


Result

The RetinaFace model successfully detects human faces in the input image and highlights each detected face using a bounding box.
