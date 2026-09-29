import cv2

face_cascade = cv2.CascadeClassifier("/home/enigmatix/opencv_project/8_face_object_detection/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    """
    detectMultiScale() -> Scan and detect Faces
    1.1 -> balance not too small blind

    minNeighbors -> this is for security 5 means average and most commonly use security
    3 means loose security and 6 means more strict security
    """
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("WebCame Face Detection", frame)

    if cv2.waitKey(1) &0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()