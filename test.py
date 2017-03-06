from HSVTrackbar import HSVTrackbar
import cv2
import numpy as np
import Queue

HSV_WINDOW = 'hsv'
cv2.namedWindow(HSV_WINDOW)
queue = Queue.Queue(maxsize=5)

imgPath = 'egg3.jpg'
original = cv2.imread(imgPath)
original = cv2.resize(original, (640, 480))

s = HSVTrackbar(queue, HSV_WINDOW, original)

print 'main continue'

while True:
    img = queue.get()
    cv2.imshow(HSV_WINDOW, img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        s.stop()
        kernel = np.ones((3, 3), np.uint8)
        i = cv2.erode(img, kernel, iterations=1)

        blur = cv2.GaussianBlur(i, (3, 3), 0)
        #cv2.imwrite('filtered.jpg', blur)
        break

cv2.destroyAllWindows()
