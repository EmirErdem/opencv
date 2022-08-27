#normal threshold kullanmadık çünkü görselde kullanamız gerekn yerlerde gölge var ve belli eşik değerini ayarlarsak o kısımlar siyah olacaktır.
import cv2

img0 = cv2.imread("image.jpeg")

img = cv2.imread("image.jpeg",0)

_,thresh = cv2.threshold(img,75,255,cv2.THRESH_BINARY) #deneme için yazılmış.

athresoshold_mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)#11 piksele bakıcaz. 3 değeri dökümantasyondan bakıldı matematiksel olarak araştır.
athresoshold_gaussian = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)

cv2.imshow("adaptiveThreshold gausian",athresoshold_gaussian)
cv2.imshow("adaptive thresh mean",athresoshold_mean)
cv2.imshow("thresh",thresh)
cv2.imshow("image",img)
cv2.imshow("image0",img0)
cv2.waitKey(0)
cv2.destroyAllWindows()

