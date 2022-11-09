from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import imutils
import face_recognition

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

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), maxSize=(600,600))

        for(x,y,ancho,alto) in faces:
            cv2.rectangle(frame,(x,y),(x+ancho,y+alto),(255,0,0),3)


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