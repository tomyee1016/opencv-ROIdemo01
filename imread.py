import cv2
import numpy as np


src =cv2.imread('e:/cat.jpg')
new =cv2.resize(src,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)#对原图像进行缩小
cv2.namedWindow('cat')
cv2.imshow('cat',new)
face =new[75:330,330:630]#其中75:330为所选区域高度的范围，330:630为宽度的范围
gray =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
backface =cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
new[75:330,330:630] =backface
cv2.imshow('face',new)
cv2.waitKey(0)
cv2.destroyAllWindows()