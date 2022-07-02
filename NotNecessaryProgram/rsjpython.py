#!/usr/bin/env python
# -*- coding: utf-8 -*
import numpy as np
import cv2
from cv2 import aruco

def main():
    # マーカーサイズ
    # マーカーの辞書選択
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    img = cv2.imread("./data/ex/ex1.png")
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary)
    img_markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)
    #img1 = img[corners[0][0][0][1] : corners[0][0][0][1]+10, corners[0][0][0][0]: corners[0][0][0][0]+5]
    print(int(corners[0][0][0][1]))
    img1 = img[int(corners[0][0][0][1])-3 : int(corners[0][0][0][1])+8 ,int(corners[0][0][0][0])+73 : int(corners[0][0][0][0])+470]
    mmbypix=75/(corners[0][0][0][0]-corners[0][0][1][0])
    cv2.imshow('drawDetectedMarkers', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

