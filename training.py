import cv2
import os

import numpy as np

personas = ['Ocampo','Castro', 'Gomez']
faces=[]
labels=[]
archivos = os.listdir("Faces")

for rostro in archivos:
    image = cv2.imread("Faces/"+rostro)
    image_fixed = cv2.resize(image,(150,150),interpolation=cv2.INTER_CUBIC)
    image_gray = cv2.cvtColor(image_fixed,cv2.COLOR_BGR2GRAY)
    if (rostro.startswith("ocampo")):
        labels.append(0)
    elif (rostro.startswith("castro")):
        labels.append(1)
    else:
        labels.append(2)
    faces.append(image_gray)

face_eigen = cv2.face.EigenFaceRecognizer_create()
face_eigen.train(faces,np.array(labels))
face_eigen.write("training-eigen.xml")


#face_fisher = cv2.face.FisherFaceRecognizer_create()
#face_fisher.train(faces,np.array(labels))
#face_fisher.write("training-fisher.xml")

face_lbph = cv2.face.LBPHFaceRecognizer_create()
face_lbph.train(faces,np.array(labels))
face_lbph.write("training-lbph.xml")