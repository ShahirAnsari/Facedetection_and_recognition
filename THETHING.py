# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:17:39 2017

@author: Walatima
"""

from tkinter import *
import csv
import cv2
import numpy as np
import threading
import tkinter.messagebox
from PIL import ImageTk, Image
import os

#from aboutWindow import Ui_AboutUs

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('train/learnedData.yml')
cascadePath = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascadePath);


def surveillance():
    cam = cv2.VideoCapture(0)
    while True:
        
        ret,img=cam.read()
        count=0
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            count = count+1
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray=gray[y:y+h, x:x+w]
            roi_color=img[y:y+h, x:x+w]
            #eyes=eye_cascade.detectMultiScale(roi_gray)
            #for (ex,ey,ew,eh) in eyes:
                #print()
            cv2.imshow('img',img)
            print('number of faces =' +str(count))
            k=cv2.waitKey(30)&0xff
            if k==27:
                break  


def identify():
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    known = 0
    unknown = 0
    allid =[]
    count = 0
    while True:
        known = 0
        unknown = 0
        s=[]
        
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            #cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)........use when to detect all.........
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            #print (Id);
            if(conf<50):
                if(Id>0 and Id<3):
                    known = known +1
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
                    #readdata(Id)
                    with open('peopledata.csv','r', newline = '') as fp:
                        print('open')
                        for line  in fp:
                            #print(line)
                            #print(line[5])
                            word = line.split(',')
                            #print(word[1])
                            if(word[1] == str(Id)):  # .........if id == 1  just in case
                                print('NAME='+word[2]+' '+word[3])
                                name = str(word[2])
                                fname = str(word[2])
                                lname = str(word[3])
                                code = str(word[4])
                                sex = str(word[5])
                                stat = str(word[6])
                                if Id in allid:
                                    print(allid)
                                else:
								
                                    if(count==0):
                                        allid = allid + [Id]
                                        name = str(Id)
                                        img1 = ImageTk.PhotoImage(Image.open("dbImg/"+name+".jpg"))# check this<<<-----
                                        img1panel = Label(img1frame, image = img1)
                                        img1panel.pack(side = TOP, fill = X)
                                        
                                        name1 = Label(img1frame, text="FIRST NAME : "+fname, bg="gray", fg="white", font=("Helvetica",10 ))
                                        name1.pack(side = TOP, fill=X)
                                        name2 = Label(img1frame, text="LAST NAME : "+lname, bg="gray", fg="white", font=("Helvetica",10 ))
                                        name2.pack(side = TOP, fill=X)
                                        code1 = Label(img1frame, text="CODE : "+code, bg="gray", fg="white", font=("Helvetica",10 ))
                                        code1.pack(side = TOP, fill=X)
                                        sex1 = Label(img1frame, text="SEX : "+sex, bg="gray", fg="white", font=("Helvetica",10 ))
                                        sex1.pack(side = TOP, fill=X)
                                        stat1 = Label(img1frame, text="STATUS : "+stat, bg="gray", fg="white", font=("Helvetica",10 ))
                                        stat1.pack(side = TOP, fill=X)
                                        count = count + 1
                                    elif(count==1):
									
                                        allid = allid + [Id]
                                        name = str(Id)
                                        img2 = ImageTk.PhotoImage(Image.open(name+".jpg"))
                                        img2panel = Label(img2frame, image = img2)
                                        img2panel.pack(side = TOP, fill = X)
                                        
                                        name2 = Label(img2frame, text="FIRST NAME : "+fname, bg="gray", fg="white", font=("Helvetica",10 ))
                                        name2.pack(side = TOP, fill=X)
                                        name2 = Label(img2frame, text="LAST NAME : "+lname, bg="gray", fg="white", font=("Helvetica",10 ))
                                        name2.pack(side = TOP, fill=X)
                                        code1 = Label(img1frame, text="CODE : "+code, bg="gray", fg="white", font=("Helvetica",10 ))
                                        code1.pack(side = TOP, fill=X)
                                        sex1 = Label(img1frame, text="SEX : "+sex, bg="gray", fg="white", font=("Helvetica",10 ))
                                        sex1.pack(side = TOP, fill=X)
                                        stat1 = Label(img1frame, text="STATUS : "+stat, bg="gray", fg="white", font=("Helvetica",10 ))
                                        stat1.pack(side = TOP, fill=X)
                                        count = count + 1
                                    elif(count==2):
									
                                        allid = allid + [Id]
                                        name = str(Id)
                                        img3 = ImageTk.PhotoImage(Image.open(name+".jpg"))
                                        img3panel = Label(img3frame, image = img3)
                                        img3panel.pack(side = TOP, fill = X)
                                        
                                        name3 = Label(img3frame, text="FIRST NAME : "+fname, bg="gray", fg="white", font=("Helvetica",10 ))
                                        name3.pack(side = TOP, fill=X)
                                        name3 = Label(img3frame, text="LAST NAME : "+lname, bg="gray", fg="white", font=("Helvetica",10 ))
                                        name3.pack(side = TOP, fill=X)
                                        code1 = Label(img1frame, text="CODE : "+code, bg="gray", fg="white", font=("Helvetica",10 ))
                                        code1.pack(side = TOP, fill=X)
                                        sex1 = Label(img1frame, text="SEX : "+sex, bg="gray", fg="white", font=("Helvetica",10 ))
                                        sex1.pack(side = TOP, fill=X)
                                        stat1 = Label(img1frame, text="STATUS : "+stat, bg="gray", fg="white", font=("Helvetica",10 ))
                                        stat1.pack(side = TOP, fill=X)
                                        count = count + 1
                                        
            else:
                Id="*"
                unknown = unknown + 1
                cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)       #________UNKNOWN_________
            cv2.putText(im,str(Id), (x,y+h),font, 1, (0,50,255), 2, cv2.LINE_AA)
        cv2.imshow('im',im)
        print('Known = '+str(known)+' Unknown ='+str(unknown))
        print(s) #.........................................
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    
def recordcam(self):
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('recor.avi', fourcc , 15.0, (640,480))

        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('CAMERA',gray)
            out.write(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
        
#surveillance()



def readdata(id1):
    print(id1)
    with open('peopledata.csv','r', newline = '') as fp:
        print('open')
        for line  in fp:
            #print(line)
            #print(line[5])
            word = line.split(',')
            #print(word[1])
            if(word[1] == str(Id)):  # ..........if id == 1  just in case
                print('NAME='+word[2]+' '+word[3])
                name = str(word[2])
                if(count == 1):
                    img1 = ImageTk.PhotoImage(Image.open("2.jpg"))
                    img1panel = Label(img1frame, image = img1)
                    img1panel.pack(side = TOP, fill = X)
                
                    name1 = Label(img1frame, text="NAME : "+name, bg="gray", fg="white", font=("Helvetica",10 ))
                    name1.pack(side = TOP, fill=X)
                    count = count + 1
                elif(count == 2):
                    img2 = ImageTk.PhotoImage(Image.open("2.jpg"))
                    img2panel = Label(img1frame, image = img1)
                    img2panel.pack(side = TOP, fill = X)
                
                    name2 = Label(img1frame, text="NAME : "+name, bg="gray", fg="white", font=("Helvetica",10 ))
                    name2.pack(side = TOP, fill=X)
                    count = count + 1
                
    
            #if(word == 1):
             #   print('Nameis everything')

#identify()
def inputface():
    #print('taking')
    print(os.system("python D:/grandfinale/dataGen2.py"))
    #print(os.system("python D:/grandfinale/ente
    print('about us')
    self.aboutWindow = QtGui.QWidget()
    self.ui = Ui_AboutUs()
    self.ui.setupUi(self.aboutWindow)
    self.aboutWindow.show()
    
def closeapp():

    answer = tkinter.messagebox.askquestion('Warning!','Dude!Wanna Close the Application?')

    if answer == 'yes':
        winx.destroy()

def trainer():
    print(os.system("python D:/grandfinale/trainer.py"))
    #print(os.system("pyhton D:/grandfinale/enterdata2.py")) # .............TRY TO REMOVE
        
def trainthread():
    print('yeayea')
    string = 'train'
    threader(string)
    
def camthread():
    string = 'camera'
    threader(string)

def recthread():
    string = 'record'
    threader(string)

def startthread():
    print('asa')
    string = 'start'
    threader(string)

def takefacethread():
    #print('nowtaking')
    string = 'takeface'
    threader(string)
    
def threader(func): #............. Individual CALLING.........
    
    if(func == 'camera'):
        t = threading.Thread(target = surveillance)
    elif(func == 'record'):
        print('recrding')
        t = threading.Thread(target = add_property)
    elif(func == 'start'):
        t = threading.Thread(target = identify)
    elif(func == 'takeface'):
        t = threading.Thread(target = inputface)
    elif(func == 'train'):
        t = threading.Thread(target = trainer)
    
    t.daemon = True
    t.start()

def add_property():
    print('erer')
    img1 = ImageTk.PhotoImage(Image.open("2.jpg"))

count = 1
winx = Tk()

topmenu  = Menu(winx)
winx.config(menu=topmenu)

heading = Label(winx, text="VISUAL MONITORING SYSTEM", bg="gray", fg="white", font=("Helvetica",25 ))
heading.pack(side = TOP , fill=X)

subMenu = Menu(topmenu)

topmenu.add_cascade(label="Open File", menu=subMenu)
subMenu.add_command(label="Image")
subMenu.add_command(label="Video")

subMenu.add_command(label="Close")
subMenu.add_command(label="Exit" , command = closeapp)

buttonframe = Frame(winx , background="#b22222")
buttonframe.pack(side=LEFT , fill = Y)
buttonframe.config()

camb = Button(buttonframe, text="Camera", command = camthread)
camb.pack(side = TOP, padx = 5, pady = 20)
camb.config(height = 1,width = 10)

recb = Button(buttonframe, text="Record" , command = recthread)
recb.pack(side = TOP, padx = 5, pady = 20)
recb.config(height = 1,width = 10)

recogb = Button(buttonframe, text="Start Recognize" , command = startthread)
recogb.pack(side = TOP, padx = 5, pady = 20)

takeface = Label(buttonframe , text = "Take New Data : ", bg="#b22222", fg="white", font=("Helvetica",20 ))
takeface.pack(side =TOP , padx = 5, pady = 20)
takeface.config(height = 1,width = 13)

takefaceb = Button(buttonframe, text="Take Faces" , command = takefacethread)
takefaceb.pack(side = TOP, padx = 5, pady = 20)
takefaceb.config(height = 1,width = 10)

trainb = Button(buttonframe, text="Train"  , command = trainthread)
trainb.pack(side = TOP, padx = 5, pady = 20)
trainb.config(height = 1,width = 10)

startb = Button(buttonframe, text="Start")
startb.pack(side = TOP, padx = 5, pady = 20)
startb.config(height = 1,width = 10)

img1frame = Frame(winx, width = 300 , background = "grey")#................
img1frame.pack(side = LEFT, fill = Y)
img1frame.config()

img2frame = Frame(winx , background = "grey" , width = 500)
img2frame.pack(side = LEFT , fill = Y)
img2frame.config(width = 200)

img3frame = Frame(winx , background = "grey")
img3frame.pack(side = LEFT , fill = Y)
img3frame.config(width = 200)

img4frame = Frame(winx , background = "grey")
img4frame.pack(side = LEFT , fill = Y)
img4frame.config(width = 200)

img5frame = Frame(winx , background = "grey")
img5frame.pack(side = LEFT , fill = Y)
img5frame.config(width = 200)



#cambutton3 = Button(img1frame, text="Camera3")
#cambutton3.pack(side = TOP ,fill =Y)

#cambutton4 = Button(img2frame, text="Camera4")
#cambutton4.pack(side = TOP , pady = 0, padx = 5)

#cambutton5 = Button(img3frame, text="Camera5")
#cambutton5.pack(side = TOP , pady = 0, padx = 5)

winx.minsize(1300,700);
winx.maxsize(1000,700);

winx.title("Image Analyser")
winx.mainloop()

