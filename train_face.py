import cv2
import os
import numpy as np

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

dataset_path = "faces"

faces = []
labels = []

label_map = {}
current_label = 0

for file in os.listdir(dataset_path):

    path = os.path.join(dataset_path, file)

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in detected_faces:
        face = gray[y:y+h, x:x+w]

        faces.append(face)
        labels.append(current_label)

    label_map[current_label] = file
    current_label += 1

# Train model
model = cv2.face.LBPHFaceRecognizer_create()
model.train(faces, np.array(labels))

model.save("face_model.yml")

print("Training complete ✅")