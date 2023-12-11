import cv2
from numpy import array

im = cv2.imread("piecesbruit.png")
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

PI1, HI1, _ = im.shape

imarray = array(gray)

imarray2 = imarray.copy()

for i in range(1, PI1 - 1):
    for j in range(1, HI1 - 1):
        sub_array = imarray[i - 1:i + 2, j - 1:j + 2]
        # somme des convultions
        conv = 0
        for k in range(3):
            for l in range(3):
                conv += sub_array[k, l]
        # moyenne des convultions
        moy = conv / 9
        imarray2[i, j] = moy

cv2.imwrite("piecesbruit2.png", imarray2)
