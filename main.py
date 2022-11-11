from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import imutils
import face_recognition
from deepface import DeepFace
import os

raiz = tk.Tk()
raiz.title("Trabajo final de IA")
raiz.wm_geometry("1280x720")
raiz['bg'] = '#49A'

def iniciar():
    global cap
    cap = cv2.VideoCapture(0)
    visualizar()
    print("Camara Seleccionada")

def visualizar():

    global pantalla,frame

    if cap is not None:



        #----Code face

        ret, frame = cap.read()
        frame = imutils.resize(frame, width=640)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

        face_eigen = cv2.face.EigenFaceRecognizer_create()
        face_eigen.read("training-eigen.xml")

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), maxSize=(600,600))

        face_loc = face_recognition.face_locations(frame)

        #face_image_encodings = face_recognition.face_encodings()

        if face_loc != []:
            for face_location in face_loc:

                # Age

                info = DeepFace.analyze(frame, actions=['age'], enforce_detection=False)
                edad = info['age']
                # end Age

                edadrostro="Edad: "+str(edad)

                face_frame_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
                result = face_recognition.compare_faces([face_frame_encodings], face_frame_encodings)
                new_image = frame[face_location[0]: face_location[2], face_location[3]: face_location[1]]
                image_fixed = cv2.resize(new_image, (150, 150), interpolation=cv2.INTER_CUBIC)
                image_gray = cv2.cvtColor(image_fixed, cv2.COLOR_BGR2GRAY)
                predict = face_eigen.predict(image_gray)

                print(predict)

                if predict[0] == 0:
                    if predict[1] <= 4500:
                        text = "Ocampo"
                        color = (125,220,0)
                    else:
                        text = "NaN"
                        color = (50, 50, 255)

                elif predict[0] == 1:
                    if predict[1] <= 4500:
                        text = "Castro"
                        color = (125, 220, 0)
                    else:
                        text = "NaN"
                        color = (50, 50, 255)

                elif predict[0] == 2:
                    if predict[1] <= 4500:
                        text = "Gomez"
                        color = (125, 220, 0)
                    else:
                        text = "NaN"
                        color = (50, 50, 255)

                else:
                    text = "NaN"
                    color = (50, 50, 255)

                cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 60), color, -1)
                cv2.rectangle(frame,(face_location[3], face_location[0]), (face_location[1], face_location[2]),color,2)
                #cv2.rectangle(frame, (x, y), (x + ancho, y + alto), color, 3)
                cv2.putText(frame, text, (face_location[3]+5, face_location[2] +20), 2, 0.7, (255,255,255),1)
                cv2.putText(frame, edadrostro, (face_location[3]+5, face_location[2] + 50), 2, 0.7, (255, 255, 255), 1)


        #---End code face

        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)

        tk.lblVideo.configure(image=img)
        tk.lblVideo.image = img
        tk.lblVideo.after(10, visualizar)
    else:
        cap.release()
        cv2.destroyAllWindows()


#cap.release()
#cv2.destroyAllWindows()

canvas1 = Canvas(raiz, width=680,height=560,bg='#52C7DE')
canvas1.pack(expand=NO)

labelback=Label(raiz,
    text="La camara no se ha iniciado",
    border=20,
    font=("ARIAL", 15),
    background="white",

)

labelback.place(
    x=320,
    y=60,
    height=480,
    width=640
)

tk.lblVideo = Label(raiz,
                    background="white"
              )
tk.lblVideo.place(x=320, y=60)

buttoninit = tk.Button(raiz,
    text="Encender Camara",
    foreground="#000000",
    background="#ffffff",
    command=iniciar,
    font=("ARIAL", 12),
    anchor="w"
)

buttoninit.place(x=80, y=130)


raiz.mainloop()