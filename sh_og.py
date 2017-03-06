import cv2
import numpy as np

## Reads the image and finds the contours
img = cv2.imread('Binaryegg1.jpg', 1)


imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

## Draws thw contours on the screen
cnt = contours[0]
cv2.drawContours(img,[cnt],0,(0,255,0),3)
print cnt
## Finds the longest distance of the contour shape
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)


cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
