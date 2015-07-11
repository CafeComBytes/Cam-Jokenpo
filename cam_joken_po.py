__author__ = 'Ueliton'
import numpy as np
import cv2

"""
Joken po com a camera

"""
#Camera
cap = cv2.VideoCapture(0)

cv2.namedWindow('frame1')
cv2.namedWindow('frame2')
min = 0
max = 400

cannyMin = min
cannyMax = min

#Eventos das barras.
#Estas funcoes sao chamadas todas as vezes que um valor muda na barra.
def cannyTreshouldMin(value):
    global cannyMin
    cannyMin = value

def cannyTreshouldMax(value):
    global cannyMax
    cannyMax = value

#Barras
cv2.createTrackbar('Trashold-Min', 'frame1', min, max, cannyTreshouldMin)
cv2.createTrackbar('Trashold-Max', 'frame1', min, max, cannyTreshouldMax)

while(True):
    # frame-By-Frame
    ret, frame = cap.read()

    # Operacores com os frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, cannyMin, cannyMax)
    print "Min:"+str(cannyMin)+" Max:"+str(cannyMax)
    # Resultados
    cv2.imshow('frame1',canny)
    cv2.imshow('frame2',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
