
                                            #Face Detection



import cv2 
import numpy as np 
import matplotlib.pyplot as plt# % matplotlib inline 
  
  
face_cascade = cv2.CascadeClassifier('C:/Users/Amit gupta/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/Amit gupta/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/cv2/data/haarcascade_eye.xml')
#smile_cascade = cv2.CascadeClassifier('C:/Users/Amit gupta/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/cv2/data/haarcascade_smile.xml')
#eyeglasstree_cascade=cv2.CascadeClassifier('C:/Users/Asus/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml')
#cat_cascade=cv2.CascadeClassifier('C:/Users/Asus/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/cv2/data/haarcascade_frontalcatface.xml')
def adjusted_detect_face(img): 
      
    face_img = img.copy() 
      
    face_rect = face_cascade.detectMultiScale(face_img,  
                                              scaleFactor = 1.13,
                                              minNeighbors = 5)
      
    for (x, y, w, h) in face_rect: 
        cv2.rectangle(face_img, (x, y),  
                      (x + w, y + h), (225, 25, 55), 2)
    return face_img 
def detect_eyes(img): 
      
    eye_img = img.copy()     
    eye_rect = eye_cascade.detectMultiScale(eye_img,  
                                            scaleFactor = 1.3,
                                            minNeighbors = 5)
    for (x, y, w, h) in eye_rect: 
        cv2.rectangle(eye_img, (x, y),  
                      (x + w, y + h), (225, 25, 55), 2)
    return eye_img

#def detect_eyesglasstree(img):
 #   eyeglasstree_img = img.copy()
 #   eyeglasstree_rect = eyeglasstree_cascade.detectMultiScale(eyeglasstree_img,
                                           # scaleFactor=1.13,
                                            #minNeighbors=5)
    #for (x, y, w, h) in eyeglasstree_rect:
     #   cv2.rectangle(eyeglasstree_img, (x, y),
      #                (x + w, y + h), (225, 25, 55), 2)
    #return eyeglasstree_img


#def detect_catface(img):
    #cat_img = img.copy()
   # cat_rect = cat_cascade.detectMultiScale(cat_img,
                                        #    scaleFactor=1.13,
                                         #   minNeighbors=5)
   # for (x, y, w, h) in cat_rect:
       # cv2.rectangle(cat_img, (x, y),
        #              (x + w, y + h), (225, 25, 55), 2)
    #return cat_img
#def adjusted_detect_smile(img):
      
    #smile_img = img.copy()
      
    #smile_rect = smile_cascade.detectMultiScale(smile_img,
                                              # scaleFactor =1.13,
                                              # minNeighbors = 555)
      
    #for (x, y, w, h) in smile_rect:
      #  cv2.rectangle(smile_img, (x, y),
                  #    (x + w, y + h), (255, 25, 55), 1)
          
    #return smile_img
img = cv2.imread('D:/Semester-3/Mini project.jpg')
img_copy1 = img.copy() 
img_copy2 = img.copy() 
img_copy3 = img.copy()
#img_copy4 = img.copy()
#img_copy5 = img.copy()
face = adjusted_detect_face(img_copy1) 
plt.imshow(face) 
eyes = detect_eyes(img_copy2) 
plt.imshow(eyes)
#smile=adjusted_detect_smile(img_copy3)
#plt.imshow(smile)
#cat=detect_catface(img_copy4)
#plt.imshow(cat)
#smile = adjusted_detect_smile(img_copy3) 
#plt.imshow(smile) 
eyes_face = adjusted_detect_face(img_copy3)
eyes_face = detect_eyes(eyes_face)
#eyes_face=adjusted_detect_smile(eyes_face)
#eyes_face=detect_catface(eyes_face)
#eyes_face = adjusted_detect_smile(eyes_face)
plt.imshow(eyes_face)
plt.show()
