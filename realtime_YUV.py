import time
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
while True:
    ret,frame_big = cap.read()
    frame = cv2.resize(frame_big,(int (frame_big.shape[1]/4),int(frame_big.shape[0]/4)))
    YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    YUV_channel = cv2.split(YUV)
    cv2.imshow("rgb",frame)
    cv2.imshow("y",YUV_channel[0])
    cv2.imshow("u",YUV_channel[1])
    cv2.imshow("v",YUV_channel[2])
    key = cv2.waitKey(1)
    if (key == ord('q')):
        break
    if (key == ord('h')):
        plt.clf()
        plt.hist(YUV_channel[0].ravel(),256,[0,256])
        plt.hist(YUV_channel[1].ravel(),256,[0,256])
        plt.hist(YUV_channel[2].ravel(),256,[0,256])
        plt.pause(0.001)
    if (key == ord('c')):
        cv2.imshow("Capture", frame_big)
        cv2.imwrite("capture.png",frame_big)
cap.release()
cv2.destroyAllWindows()