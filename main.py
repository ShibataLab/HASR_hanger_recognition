import cv2
import numpy as np
import math
import os
from cv2 import aruco
i=0
pos_list = []
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
# 画像のパスを指定
file_path = "./data/ari/ari5.png"

# 画像を読み込む
img = cv2.imread(file_path)

corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary)
img = img[int(corners[0][0][0][1])-3 : int(corners[0][0][0][1])+3 ,int(corners[0][0][0][0])+73 : int(corners[0][0][0][0])+470]
height = img.shape[0]
width = img.shape[1]
img = cv2.resize(img , (int(width*2), int(height*10)))
# グレースケールに変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ガウシアンフィルターをかける

# 2値化する
thres = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

cons = cv2.findContours(thres,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_NONE)[0]
# 輪郭を描画する
l = list(cons)
for index, con in enumerate(cons):
  # 面積が閾値を超えない場合、輪郭としない
    if cv2.contourArea(con) < 200:
        l.pop(index-i)
        cons = tuple(l)
        i= i+1
        continue

  # 描画処理
    cv2.polylines(img, con, True, (255, 0, 0), 3)
for con in cons:
    print(con[0][0])
    #cv2.putText(img,text=str(int(cv2.contourArea(con))),org=con[20][0],fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0, 0, 255),thickness=1,lineType=cv2.LINE_4)
    if cv2.contourArea(con) > 600:
        pos_list.append(con[20][0])
        for c in con:
            cv2.circle(img, c[0], 1, (0, 255, 0),thickness=1)
#本数
print("ハンガーの本数は",len(cons))
print("重なっている場所は",pos_list )
cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
