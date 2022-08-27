
import cv2

img1 =cv2.imread("1.jpg")
img2 =cv2.imread("2.jpg")

result = cv2.addWeighted(img1,0.4,img2,0.6,0) # img1 ve img2 agırlıklı toplam oranları toplamı 1 olması gerekir. en son daki değer gama degeridir.
#çıkarma işlemi için subtract kullan


cv2.imshow("add",result)
cv2.imshow("1", img1)
cv2.imshow("2", img2)


cv2.waitKey(0)
cv2.destroyAllWindows()