import cv2

image = cv2.imread("image.png")

roi = image[0:90,170:280]# image  dosyasının belirtilen aralıklardaki kısmını aldık.
cv2.imwrite("image2.png",roi)# oluşturudgumuz roi görselini kayıt ettik


cv2.imshow("roi",roi)
cv2.imshow("frame",image)

cv2.waitKey(0)
cv2.destroyAllWindows()