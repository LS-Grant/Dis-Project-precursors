import numpy as np
import cv2
import RPi.GPIO as GPIO
import time

# Obtain the Haar cascade data from OpenCV
faceCascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
CAMLED = 32
cap.set(3,640) # Sets width of camera stream
cap.set(4,480) # Sets height of camera stream
GPIO.setmode(GPIO.BCM) #Initilaizes the LEDs
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(17,False) #Turns off the LEDS before the system starts
GPIO.output(18,False)
GPIO.output(22,False)


while True:
    #Captures the video from the camera.
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Calls the cascade function and passed the parameters
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    # LED transition
    GPIO.output(22, False)
    GPIO.output(17,True)
    #This part draws the square around the face
    for (x,y,w,h) in faces:
        #LED Transition
        GPIO.output(17,False)
        GPIO.output(18,True)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #Verifies the captured face
        time.sleep(2)
        #LED transition
        GPIO.output(18, False)
        GPIO.output(22, True)
        #Saves the captured frame as jpeg
        cv2.imwrite('Face.jpg',img)
        
        
    #Shows video stream
    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        #When escape key is pressed the program ends
        break

cap.release()
cv2.destroyAllWindows()