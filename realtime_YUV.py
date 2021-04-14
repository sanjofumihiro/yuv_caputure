import time
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    YUV_channel = cv2.split(YUV)
    cv2.imshow("yuv",YUV)
    plt.clf()
    plt.hist(YUV_channel[0].ravel(),256,[0,256])
    plt.hist(YUV_channel[1].ravel(),256,[0,256])
    plt.hist(YUV_channel[2].ravel(),256,[0,256])
    plt.pause(0.01)
    
    key = cv2.waitKey(100)
    if (key == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()