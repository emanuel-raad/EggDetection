import cv2
import numpy as np

# Reads the image and does color filtration
img = cv2.imread('egg3.jpg',1)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

a = [0, 0, 100]
b = [180, 255, 255]

lower_white = np.array([73,0,0])
upper_white = np.array([255,255,255])

mask = cv2.inRange(hsv, lower_white, upper_white)

res = cv2.bitwise_and(img,img, mask= mask)

cv2.imwrite('eggafterfiltration.jpg', res)

# Reads the image after colour filtration and converts to gray, does threshold, opening, closing
img1 = cv2.imread('eggafterfiltration.jpg',1)

gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

kernel = np.ones((2,2),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, np.ones((2,2),np.uint8),iterations=2)

fl, fl2, fl3, ctrs = cv2.connectedComponentsWithStats(closing)

cv2.imshow('thres', closing)


# This will give us the binary image of the egg. Then we can use contours and similarity.
cv2.imwrite('Binaryegg1.jpg', closing)


cv2.waitKey(0)
cv2.destroyAllWindows()
