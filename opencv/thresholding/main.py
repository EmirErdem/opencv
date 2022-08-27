import cv2



img = cv2.imread("image1.jpeg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


_, threshold = cv2.threshold(img,127,255,cv2.THRESH_BINARY)# 127 den kucuk olan degelri 0(siyah) a eşitledi 127den büyük olan değerleri  255(beyaz) e eşitledi.
_, thresh_inv = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)# 127 den kucuk olan degelri 255 e eşitledi 127den büyük olan değerleri  0 a eşitledi.


_, tozero = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) # 127 den küçük değerleri 0 a eşitledik  127den büyük değerleri değiştirmedi aynen kaldı
_,tozero_inv = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)# 127 den küçük değerleri aynı kalıyor 127den büyük değerleri 0 a eşitledik.



cv2.imshow("to zero inv",tozero_inv)
cv2.imshow("to zero",tozero)
cv2.imshow("thresh inv",thresh_inv)
cv2.imshow("thresh ",threshold)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





