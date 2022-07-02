#!/usr/bin/env python
# -*- coding: utf-8 -*
import numpy as np
import cv2
from cv2 import aruco

def main():
    # マーカーサイズ
    # マーカーの辞書選択
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    img = cv2.imread("./data/ari/ari1.png")
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary)
    img_markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)
    #img1 = img[corners[0][0][0][1] : corners[0][0][0][1]+10, corners[0][0][0][0]: corners[0][0][0][0]+5]
    print(int(corners[0][0][0][1]))
    img1 = img[int(corners[0][0][0][1])-3 : int(corners[0][0][0][1])+8 ,int(corners[0][0][0][0])+73 : int(corners[0][0][0][0])+470]
    #img1=img
    #mmbypix=75/(corners[0][0][0][0]-corners[0][0][1][0])
    hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    v = (v-np.mean(v)) / np.std(v) * 20 + 64
    result = np.array(v, dtype=np.uint8)
    hsv = cv2.merge((h,s,result))
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('drawDetectedMarkers', rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

