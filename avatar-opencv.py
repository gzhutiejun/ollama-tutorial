import cv2
import dlib
from PIL import Image
import numpy as np

# Load the dlib face detector
detector = dlib.get_frontal_face_detector()

# Function to detect and extract faces from images
def extract_face(image_path):
    image = cv2.imread(image_path)
    faces = detector(image)
    if len(faces) > 0:
        face = faces[0]  # Extract the first face found
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        face_image = image[y:y+h, x:x+w]
        return cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
    else:
        return None

# Paths to your images
image_paths = ['data/hh1.jpeg','data/hh2.jpeg']

# Extract faces and store them
faces = []
for path in image_paths:
    face = extract_face(path)
    if face is not None:
        faces.append(face)

# Create a composite image by stacking faces horizontally
if faces:
    composite_face = np.hstack(faces)
    composite_image = Image.fromarray(composite_face)
    composite_image.save('hh_avatar.jpg')
    composite_image.show()
else:
    print("No faces detected in the images.")