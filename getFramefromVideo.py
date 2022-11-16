import cv2     
import cv2 as cv
import numpy as np


# 本代码用于从视频中截取图片用于训练

inputPath = 'C:/Users/lenovo/Desktop/jjVideos/24.mp4'
outputPath = 'C:/Users/lenovo/Desktop/jjImages/'
start_count = 0
start_num_name = 1167  # 输出名字由start_num_name与video_name组成
video_name = ''
stride = 4 # 步长 q

vc = cv.VideoCapture(inputPath)
totalframe = vc.get(cv2.CAP_PROP_FRAME_COUNT)
print('This video has ' + str(totalframe) + ' frames')

rval, frame = vc.read()
num = start_num_name
count = start_count

while rval:
    count += 1
    rval, frame = vc.read()

    if count % stride == 0:
        cv.imshow('output', frame)
        k = cv.waitKey(0)
        if k == 115:  # 按键s保存
            cv.imwrite(outputPath + video_name + str(num) +'.jpg', frame)
            num += 1
        else:
            s = round(count/totalframe*100, 2)
            print(str(s) + '%')
            continue
        print(num)

cv.destroyAllWindows()