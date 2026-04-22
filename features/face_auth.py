import cv2
import time

def authenticate_face():

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_eye.xml'
    )

    model = cv2.face.LBPHFaceRecognizer_create()
    model.read("face_model.yml")

    video = cv2.VideoCapture(0)

    print("Scanning face...")

    start_time = time.time()

    while True:
        ret, frame = video.read()

        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            if w < 100 or h < 100:
                continue

            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))

            eyes = eye_cascade.detectMultiScale(face)
            print("Eyes:", len(eyes))

            blur = cv2.Laplacian(face, cv2.CV_64F).var()
            print("Blur:", blur)


            label, confidence = model.predict(face)

            print("Confidence:", confidence)

            if confidence < 65:
                print("Authorized")
                video.release()
                cv2.destroyAllWindows()
                return True

        cv2.imshow("Face Login", frame)

        if time.time() - start_time > 10:
            print("Timeout")
            break

        if cv2.waitKey(1) == 27:
            break

    video.release()
    cv2.destroyAllWindows()

    print("Access Denied ")
    return False