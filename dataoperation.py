# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:17:39 2017

@author: Walatima
"""


import csv

def writedata():
    with open('peopledata2.csv','w', newline = '') as fp:
        a = csv.writer(fp)
        thing = [1]
        thing = thing+[2]
        thing = thing + [3]
        data = thing

        a.writerows(data)

#writedata()


def readdata():
    with open('peopledata.csv','r', newline = '') as fp:
        print('open')
        for line  in fp:
            #print(line)
            #print(line[5])
            word = line.split(',')
            #print(word[1])
            if(word[1] == str(1)):  # if id == 1  just in case
                print('NAME='+word[2]+' '+word[3])
            
    
            #if(word == 1):
            #   print('Nameis everything')(['S.no','Id','First Name','Last Name','Code','Sex','Status'],
            '''['1','1','Ben','Affleck','voo4','Male','Flying'],
            ['2','2','Karthik','Senpai','v005','Male','Thinking'],
            ['3','4','Vaibhav','Coder','v001','Male','Coding'],
            ['4','3','Abhishek','Tiwari','v003','Male','Gives no Shit'],
            ['5','5','Rauf','Khan','v002','Male','Some Work'])'''

def some():
    with open('peopledata.csv','r', newline = '') as fp:
        for line in fp:
            word=line.split(',')
            if(word[1]=='found'):
                print(line)
                fp[1][2] = '1'
                writer=csv.writer(open('peopledata.csv','w',))
                writer.writerows(fp)

#some()
#readdata()
writedata()
