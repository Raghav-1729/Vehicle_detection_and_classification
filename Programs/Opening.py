import cv2
import numpy as np
import time

kernalOp = np.ones((3,3),np.uint8)
kernalCl = np.ones((11,11),np.uint8)
#---------------------------------------------------VARIABLE DECLARATIONS-------------------------------------------------------------------------------
cap=cv2.VideoCapture("video.mp4")
fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=False,history=200,varThreshold = 90)
while(cap.isOpened()):
    ret,frame=cap.read() 
    frame=cv2.resize(frame,(900,500))
    fgmask=fgbg.apply(frame)

#------------------------------------------------------BINARIZATION----------------------------------------------------------------------------
    if ret==True:
        ret,imBin=cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernalOp) #Opening :E->D
        cv2.imshow('Morpgology Operations',mask)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernalCl) #Closing :D->E
  
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    

cap.release()
cv2.destroyAllWindows()
