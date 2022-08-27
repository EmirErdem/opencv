import cv2

img = cv2.imread("images.jpeg")


gaussian = cv2.GaussianBlur(img,(15,15),0)#  (yapıcalak gorsel, çekirdek boyutu ,sigma)  genel blurlama yapıyor.

median = cv2.medianBlur(img,5) # gürültüyü gidermede kullanılır.

bila = cv2.bilateralFilter(img,20,120,75) #kenar koruyarak blurlama performansı gaustan iyidr. kenarları korur. gaus her şeyi blurlar.


blur = cv2.blur(img,(5,5))

cv2.imshow("blur",blur)
cv2.imshow("bila",bila)
cv2.imshow("median",median)
cv2.imshow("gassuian",gaussian)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
