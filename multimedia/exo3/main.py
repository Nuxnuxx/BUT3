import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


pixel_values = gray_image.ravel() 
plt.hist(pixel_values, bins=256, range=(0, 256), density=True, color='gray', alpha=0.7)

x = np.linspace(0, 255, 256)

s = 2
m1 =15 

g1 = 1 * np.exp(-(x-m1)**2/(2*s**2))

plt.plot(x, g1, label='gauss', color='blue')
plt.title('Histogram')
plt.xlabel('Valeur')
plt.ylabel('Pixel')

plt.savefig('diag.png')
