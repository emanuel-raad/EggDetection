import cv2
import numpy as np
import threading
import time
import Queue

class HSVTrackbar:

    def __init__(self, queue, window, image):
        self.image = image
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.interval = 5.0/1000.0
        self.queue = queue
        self.window = window

        cv2.createTrackbar('l_h', self.window, 0, 255, self.nothing)
        cv2.createTrackbar('l_s', self.window, 0, 255, self.nothing)
        cv2.createTrackbar('l_v', self.window, 0, 255, self.nothing)

        cv2.createTrackbar('h_h', self.window, 0, 255, self.nothing)
        cv2.createTrackbar('h_s', self.window, 0, 255, self.nothing)
        cv2.createTrackbar('h_v', self.window, 0, 255, self.nothing)

        thread = threading.Thread(target=self.run)
        thread.daemon = True
        self.isRunning = True
        thread.start()

    def nothing(self, x):
        pass

    def stop(self):
        print 'stopping HSVTrackbar'
        self.isRunning = False

    def run(self):
        while self.isRunning:
            l_h = cv2.getTrackbarPos('l_h', self.window)
            l_s = cv2.getTrackbarPos('l_s', self.window)
            l_v = cv2.getTrackbarPos('l_v', self.window)

            h_h = cv2.getTrackbarPos('h_h', self.window)
            h_s = cv2.getTrackbarPos('h_s', self.window)
            h_v = cv2.getTrackbarPos('h_v', self.window)

            low = np.array([l_h, l_s, l_v])
            high = np.array([h_h, h_s, h_v])

            mask = cv2.inRange(self.hsv, low, high)
            res = cv2.bitwise_and(self.image, self.image, mask=mask)

            #cv2.imshow(self.window, res)
            #time.sleep(self.interval)
            self.queue.put(res)
