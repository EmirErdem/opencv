import cv2
import numpy as np

img = cv2.imread("2080-ti.jpg")
img = cv2.pyrDown(img)  # görseli küçülttük

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #hsv renk uzayına dönüştürdük

low = np.array([23,100,50]) #  görsel sarı oldugu için skaladan bakarak 23  ve 35 arasındaki değerleri aldık.
up = np.array([35,255,255]) #  görsel sarı oldugu için skaladan bakarak 23  ve 35 arasındaki değerleri aldık.

mask = cv2.inRange(hsv,low,up) #  hsv görselinin low ve up değer aralıklarına göre atama yaptık.
mask = cv2.medianBlur(mask,5) #  görseli daha iyi hale geitrmek için blurlama yaptık.

fil = cv2.bitwise_and(img,img,mask=mask) #and işlemi kullanarak orjinal görselleri mask degerlerine göre karşılaştırdık.

cv2.imshow("hsv",hsv)
cv2.imshow("filter",fil)
cv2.imshow("mask",mask)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()