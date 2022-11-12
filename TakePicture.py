import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

i = 69
while cap.isOpened():
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30),maxSize=(600, 600))
    for (x, y, ancho, alto) in faces:
        key = cv2.waitKey(1)
        if key == ord("c"):
            print("Recorte")
            i += 1
            nuevaimg = frame[y:y + alto, x:x + ancho,]
            #
            cv2.imwrite("Faces/ocampo" + str(i) + ".jpg", nuevaimg)
        cv2.rectangle(frame, (x, y), (x + ancho, y + alto), (255, 0, 0), 3)

        # cv2.waitKey(2)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
        # ---End code face


cap.release()
cv2.destroyAllWindows()
