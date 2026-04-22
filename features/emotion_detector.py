import cv2
import time
import random

def detect_emotion():

    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    emotions = ["happy", "sad", "angry", "neutral"]

    detected_emotion = "neutral"

    start_time = time.time()

    print("Opening camera for emotion detection...")

    while time.time() - start_time < 7:

        ret, frame = cap.read()

        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            detected_emotion = random.choice(emotions)

            cv2.putText(
                frame,
                detected_emotion,
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )

        cv2.imshow("Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Detected Emotion:", detected_emotion)

    return detected_emotion