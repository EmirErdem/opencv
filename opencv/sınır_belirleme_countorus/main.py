import cv2
import numpy as np
img=np.zeros((600,800,1),np.uint8)
img2=np.zeros((600,800,3),np.uint8)

cv2.rectangle(img,(200,200),(600,400),255,-1,) 


contours,_= cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #SIMPLE sadece 4 noktayı secer NONE  bütün sınırın etrafını dolaşır. 

for cnt in contours:
    for i in cnt:  # bütün piksellere ulaşmak için gezindik
        x,y=i[0]   # matrislerden kurtulmak iiçin ilk elemanı aldık sadece ve x,y ye atadık
        cv2.circle(img2,(x,y),5,(0,0,255),-1) # her piksele daire çizdik 
        #img2[y,x] =[0,0,255] olarak yaparsak çizgi çizer.





cv2.imshow("img1",img)
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
