import cv2
import numpy as np

img=np.zeros((600,800,3,),np.uint8)

cv2.rectangle(img,(200,200),(400,400),(255,0,0),-1)
cv2.line(img,(0,0),(800,600),(0,255,0),3)
cv2.circle(img,(300,300),10,(0,0,255),3)
cv2.putText(img,"Emir ERDEM",(190,100),cv2.FONT_HERSHEY_PLAIN,2,(255,255,0))



cv2.imshow("frame",img)

cv2.waitKey(0)
cv2.destroyAllWindows()