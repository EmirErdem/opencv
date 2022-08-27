import cv2



img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# görseli griye cevirdik.


hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)# çevirme sebeimiz filtreleme yaparken bgr dan daha kolay olmasıdır. bgr da 3 farklı değişkenle uğraşıyorz.


cv2.imshow("hsv",hsv)
cv2.imshow("gray",gray)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

