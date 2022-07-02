#!/usr/bin/env python
# -*- coding: utf-8 -*
import numpy as np
import cv2
from cv2 import aruco

#This is rate
#mmbypix=75/(corners[0][0][0][0]-corners[0][0][1][0])
def hsvstd (img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    v = (v-np.mean(v)) / np.std(v) * 20 + 64
    result = np.array(v, dtype=np.uint8)
    hsv = cv2.merge((h,s,result))
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return rgb
def imgfix(path):
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    img=cv2.imread(path,1)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary)
    img_markers = aruco.drawDetectedMarkers(img.copy(), corners, ids)
    imga = img[int(corners[0][0][0][1])-3 : int(corners[0][0][0][1])+8 ,int(corners[0][0][0][0])+73 : int(corners[0][0][0][0])+470]
    imgb = hsvstd(imga)
    print("success")
    height = imga.shape[0]
    width = imga.shape[1]
    imga = cv2.resize(imga , (int(width*2), int(height*10)))
    return imga

def main():
    img1 = imgfix("./data/nashi/nashi1.png")
    img2 = imgfix("./data/ari/ari2.png")
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    fgmask = fgbg.apply(img1)
    fgmask = fgbg.apply(img2)
    cv2.imshow('frame',fgmask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()

