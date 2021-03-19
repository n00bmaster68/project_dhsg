import cv2 as cv
from matplotlib import pyplot as plt

# Load image in grayscale
img = cv.imread('test.jpg',0)

# threshold the image
thresh = cv.threshold(img,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)[1]

# display the image
plt.imshow(thresh, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()