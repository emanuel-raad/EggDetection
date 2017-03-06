import cv2
import numpy as np
from Color import randomColor
import time

start_time = time.time()

def filterAreaLow(contours, thresLow):
    filteredAreas = []
    for i in contours:
        if cv2.contourArea(i) >= thresLow:
            filteredAreas.append(i)
    return filteredAreas

## Reads the image and finds the contours
img = cv2.imread('Binaryegg1.jpg', 1)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = filterAreaLow(contours, 5000)
## Draws thw contours on the screen

for i in range(len(contours)):
	cnt = contours[i]
	color = randomColor()
	cv2.drawContours(img,[cnt],0,color,3)
	
	rows,cols = img.shape[:2]
	[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
	lefty = int((-x*vy/vx) + y)
	righty = int(((cols-x)*vy/vx)+y)
	try:
		img = cv2.line(img,(cols-1,righty),(0,lefty),color,2)
	except:
		print i
		print lefty
		print righty

## Finds the longest distance of the contour shape

print("--- %s seconds ---" % (time.time() - start_time))

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
