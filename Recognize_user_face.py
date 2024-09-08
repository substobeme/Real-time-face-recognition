import cv2
import mysql.connector
from datetime import datetime, timedelta


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="face_info"
)
cursor = db_connection.cursor()

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recognizer.ymnl')

width, height = 220, 220
camera = cv2.VideoCapture(0)


last_recognized = {
    "Subha": datetime.now() - timedelta(seconds=2),
    "Ashutosh": datetime.now() - timedelta(seconds=2),
    "Akash": datetime.now() - timedelta(seconds=2)
}

while True:
    check, frame = camera.read()
    frame_gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detections = face_detector.detectMultiScale(frame_gr, scaleFactor=1.07, minNeighbors=8, minSize=(84, 84))

    for (x, y, w, h) in detections:
        frame_face = cv2.resize(frame_gr[y:y + h, x:x + w], (width, height))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        pred, conf = face_recognizer.predict(frame_face)
        identity = "unknown"

        if pred == 1 and conf > 0.95:
            identity = "Subha"
        elif pred == 2 and conf > 0.95:
            identity = "Ashutosh"
        elif pred == 3 and conf > 0.95:
            identity = "Akash"

        cv2.putText(frame, identity, (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 1)

        if identity != "unknown":
            current_time = datetime.now()
            if current_time - last_recognized[identity] >= timedelta(seconds=1):

                insert_query = "INSERT INTO face(Name, Time, Photo) VALUES (%s, %s, %s)"
                image_bytes = cv2.imencode('.jpg', frame_face)[1].tobytes()
                cursor.execute(insert_query, (identity, current_time, image_bytes))
                db_connection.commit()
                last_recognized[identity] = current_time

    cv2.imshow("Recognizer", frame)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
cursor.close()
db_connection.close()
