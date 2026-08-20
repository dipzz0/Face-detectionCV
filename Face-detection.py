# Install Libraries
!pip install retina-face opencv-python-headless -q

# Import Libraries
from retinaface import RetinaFace
import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload Image
print("Upload an Image")
uploaded = files.upload()

# Read Image
image_name = list(uploaded.keys())[0]
img = cv2.imread(image_name)

# Detect Faces
faces = RetinaFace.detect_faces(img)

# Draw Bounding Boxes
if isinstance(faces, dict):
    for face in faces.values():
        x1, y1, x2, y2 = face["facial_area"]
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
# Display Output
cv2_imshow(img)
