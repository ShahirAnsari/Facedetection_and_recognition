# -*- coding: utf-8 -*-
"""
Created on Thu Mar  16 18:12:46 2017

@author: Walatima
"""


import cv2,os
import numpy as np
from PIL import Image

detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.createLBPHFaceRecognizer()
    
def getStuff(path):
    
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    Ids=[]

    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces=detector.detectMultiScale(imageNp)

        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids

  
faces,ids = getStuff('dataSet')
recognizer.train(faces,np.array(ids))
recognizer.save('train/learnedData.yml')

        

