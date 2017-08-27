# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:12:02 2016

@author: Walatima
"""

import os
import cv2

class ctakeimage():
    
    def takeimage():
        
        maxid = 0
        for file in os.listdir('dataSet'):
            #print(maxid)
            word = file.split('.')
            
            if(maxid < int(word[1])):
                maxid = int(word[1])
                print(maxid)
        
        #faceId = str(maxid + 1) #use an integer or something change this when getting a new face
        faceId = str(maxid+1)
        num=0 # just a count thing number
        cam = cv2.VideoCapture(0)
        detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
        while(True):
            ret,img = cam.read()
            cv2.imshow('frame',img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            print("1")
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                print("2")
                num=num+1
                cv2.imwrite("dataSet/User."+faceId +'.'+ str(num) + ".jpg", gray[y:y+h,x:x+w])
                print("3")
                cv2.imshow('frame',img)
        
                if cv2.waitKey(200) & 0xFF == ord('q'):
                    break
                elif (num>30): #taking 30 images for training purposes ;)
                    cam.release()
                    cv2.destroyAllWindows()
                    break
            
     
ctakeimage.takeimage()
'''def takefaces():
    with open('peopledata.csv','r', newline = '') as fp:
        print()
        for line in fp:
            word = line.split(',')
            if (word[0] == faceids):
                print(word)'''
            
