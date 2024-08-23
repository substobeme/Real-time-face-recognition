import cv2
import os


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


if face_cascade.empty():
    print("Error loading cascade files")
    exit()

camera = cv2.VideoCapture(0)
sample = 1
n_samples = 500
id = input('Type a number (ID): ')
width, height = 220, 220
print(" Press 'q' to capture.")

# Specify the directory
save_directory = r"C:\Users\ASUS\PycharmProjects\pythonProject"

# Ensure the directory exists
os.makedirs(save_directory, exist_ok=True)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture image")
        break



    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minSize=(150, 150))

    print(f"Detected {len(faces)} faces")

    for (x, y, w, h) in faces:

        face_region = frame[y:y + h, x:x + w]
        




        face_img = cv2.resize(frame[y:y + h, x:x + w], (width, height))
        save_path = os.path.join(save_directory, f"person.{id}.{sample}.jpg")
        success = cv2.imwrite(save_path, face_img)
        if success:
            print(f"[photo {sample} captured successfully]")
            sample += 1
        else:
            print(f"Failed")

    cv2.imshow("Face", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or sample > n_samples:
        break

print("Done")
camera.release()
cv2.destroyAllWindows()

