import cv2
import numpy as np

img=cv2.imread("image.png")
opening=cv2.imread("opening.png")
closing=cv2.imread("closing.png")

kernel=np.ones((5,5),np.uint8) # (5,5) iyi bir oran genelde kullanılır.
erode= cv2.erode(img,kernel) # görselin çizgilerini inceltir.
dilate= cv2.dilate(img,kernel)# görselin çizgilerini kalınlaştırır.
opennmorp= cv2.morphologyEx(opening,cv2.MORPH_OPEN,kernel) #görselin etrafındaki pürüzzleri kaldırdı.
closingmorhp=cv2.morphologyEx(closing,cv2.MORPH_CLOSE,kernel) #görselin içindeki pürzler gitti.



cv2.imshow("closingmorhp",closingmorhp)
cv2.imshow("closing",closing)
cv2.imshow("opening",opening)
cv2.imshow("morhp open",opennmorp)
cv2.imshow("dilate",dilate)
cv2.imshow("erode",erode)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()