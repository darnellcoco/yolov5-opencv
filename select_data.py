# 此代码用于从图片和标注数据集中删除无效图片与标注

import os
import cv2 as cv

imgpath = "C:\\Users\\lenovo\\Desktop\\ball\\img\\"
labelpath = 'C:\\Users\\lenovo\\Desktop\\ball\\label\\'

cv.namedWindow('output', cv.WINDOW_NORMAL)

for root, dirs, files in os.walk(imgpath):
    for file in files:
        if file is not None:
            path = imgpath + file
            im = cv.imread(path, 1)
            cv.imshow('output', im)
            k = cv.waitKey(0)

            if k == 115: # 键盘s
                os.remove(path)
                path2 = labelpath + '.'.join(file.split('.')[0:-1]) + '.txt'
                print(path2)
                if os.path.exists(path2):
                    os.remove(path2)
                    print(path2 + ' has been removed')
            else:
                continue

cv.destroyAllWindows()
