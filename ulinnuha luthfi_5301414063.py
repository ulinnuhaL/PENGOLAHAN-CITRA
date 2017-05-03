import cv2
import numpy as np

#capture from camera at location 0
cap = cv2.VideoCapture(0)
#set the width and height, and UNSUCCESSFULLY set the exposure time
mat=np.array(cap)



while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness1 = frame+25
    invert1 =255-frame

    brightness2 = gray+25
    invert2 =255-gray
    #cv2.imshow("thresholded", imgray*thresh2)
    cv2.imshow('gambar asli(grayscale)', gray)
    cv2.imshow('gambar asli(RGB)', frame)
    cv2.imshow('brightness(grayscale)', brightness2)
    cv2.imshow('invert(grayscale)', invert2)
    cv2.imshow('brightness(RGB)', brightness1)
    cv2.imshow('invert(RGB)', invert1)
    
    key = cv2.waitKey(10)
    if key == 27:
        break
cv2.destroyAllWindows() 
cv2.VideoCapture(0).release()
