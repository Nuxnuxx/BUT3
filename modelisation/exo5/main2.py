import cv2
import numpy as np

I1 = cv2.imread("./I1.jpg")
I2 = cv2.imread("./I2.jpg")

PI1, HI1, _ = I1.shape
PI2, HI2, _ = I2.shape

H = np.array([[1, 0, 0], [0, 1, 100], [0, 0, 1]])

width = PI1 + PI2
height = HI1 + HI2

channels = 3
mosaic = np.ones((height, width, channels), dtype=np.uint8) * 255

for x1 in range(PI1):
    for y1 in range(HI1):
        new_coords = H @ np.array([x1, y1, 1])
        new_x, new_y, _ = (new_coords / new_coords[2]).astype(int)
        mosaic[new_y, new_x] = I1[y1, x1]

# Uncomment this block if you want to overlay I2 on top
# for x2 in range(PI2):
#     for y2 in range(HI2):
#         mosaic[y2, x2] = I2[y2, x2]

cv2.imshow('Mosaic', mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()
