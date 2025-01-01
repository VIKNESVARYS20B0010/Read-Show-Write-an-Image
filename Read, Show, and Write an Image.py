import cv2
img = cv2.imread("nature.jpg")
cv2.imshow('show',img)
cv2.imwrite('photo.png',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
