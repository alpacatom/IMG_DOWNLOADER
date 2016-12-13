# -*- coding: utf-8 -*-

import requests
import json
import os
import wget
import cv2
#import numpy as np
import sys
import re

args = sys.argv

if len(args) < 4 :
    print "Usage : $ python trim_image.py [original images-dir] [trim-dir] [resize-dir]"
    exit(1)

#Name for face_path
ORIGIN= args[1]
TERM  = args[2]
TERM2 = args[3]

#absolute path
path = '**PATH**'

#output path for images
output_path = path + ORIGIN + '/'

#output path for face images
face_path = path + TERM + '/'
resize_path = path + TERM2 + '/'

#Path to animeface.xml
cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/lbpcascade_animeface.xml"

#parameter for face line size (you can tune this)
FACELINE_SIZE = 10
IMG_SIZE = 32

def img_trim() :
    print "Trimming images..."
    files = os.listdir(output_path)
    color = (255, 255, 255)
    counter = 0
    for file in files :
        jpg = re.compile("jpg")
        png = re.compile("png")

        if (jpg.search(file) or png.search(file)) :            
            image = cv2.imread(output_path+file)

            if image is None:
                print "Failed to load : " + file
                continue

            print output_path+file            
            print image.shape
            image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
            cascade = cv2.CascadeClassifier(cascade_path)
            facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
        
            if len(facerect) > 0:    
                for rect in facerect:    
                    x = rect[0]
                    y = rect[1]
                    width = rect[2]
                    height = rect[3]
                    dst = image[y-FACELINE_SIZE:y+height+FACELINE_SIZE, x-FACELINE_SIZE:x+width+FACELINE_SIZE] 
                    cv2.imwrite(face_path+str(counter)+"_face.jpg", dst)                    
                    counter += 1

def img_resize() :
    print "Resizing images..."
    files = os.listdir(face_path)  
    size = (IMG_SIZE, IMG_SIZE)
    counter = 0
    for file in files :
        image = cv2.imread(face_path+file)        
        if image is None:
            print "Failed to load" + file
            continue
        converted = cv2.resize(image, size)
        cv2.imwrite(resize_path+str(counter)+'_face_32x32.jpg', converted)
        counter += 1

def run() :    
    #img_trim()
    img_resize()
if __name__ == '__main__':
    run()
