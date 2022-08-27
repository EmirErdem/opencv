import cv2 as cv

import numpy as np


cap = cv.VideoCapture(0)



def renksec():


 while True:

    ret ,e = cap.read()
    e = cv.rectangle(e,(0,0),(0,0),(1,90,3),3)
    J = e[0:200,0:200,:]
    hsv=cv.cvtColor(J,cv.COLOR_BGR2HSV)
    alt = np.array([170,50,50])
    ust = np.array([180,255,255])
    mask = cv.inRange(hsv,alt,ust)
    feat = np.mean(mask)

    mask1= cv.bitwise_and(J, J, mask=mask)
    cv.putText(mask1,str(feat),(50,50),1,2,[0,0,255],1)

    if feat > 5:
        cv.putText(e,'KIRMIZI',(10,250),2,2,[0,0,255],3)
        [x,y]=np.where(mask == 255)
        x_m=np.mean(x).astype(np.uint8)

        y_m=np.mean(y).astype(np.uint8)


        e =cv.circle(e,(y_m,x_m),50,(255,0,0),3)
    else:
        cv.putText(e,'Renk Yok',(10,250),2,2,[255,255,255],3)
    cv.imshow("e",e)
    cv.imshow("j",J)
    cv.imshow("hsv",hsv)
    cv.imshow("mask",mask)
    cv.imshow('mask1',mask1)
   
    if cv.waitKey(27) & 0xFF == ord('q'):
        break
 cv.destroyAllWindows()
 cap.release()


renksec()