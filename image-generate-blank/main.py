import cv2
import numpy as np

width = 640
height = 920
img = np.zeros([height, width, 3], dtype=np.uint8)
img.fill(128)  # or img[:] = 128

filename = 'generated-image.jpg'
cv2.imwrite(filename, img)
