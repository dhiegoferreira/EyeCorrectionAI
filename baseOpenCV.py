# Basic example of what you'll learn:
import cv2
import numpy as np

# Read an image
img = cv2.imread('eye_image.jpg')
# Basic operations
resized = cv2.resize(img, (300, 300))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Display image
cv2.imshow('Image', img)
cv2.waitKey(0)




