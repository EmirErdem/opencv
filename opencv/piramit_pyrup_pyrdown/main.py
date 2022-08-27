import cv2



img = cv2.imread("1.jpg")

up = cv2.pyrUp(img)
down = cv2.pyrDown(img)


cv2.imshow("down",down)
cv2.imshow("pyrup",up)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





