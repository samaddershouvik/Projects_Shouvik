import cv2
import numpy as np

# load image
img = cv2.imread('Jamuna river data1973.png')

# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

# create mask for blue color in hsv
# blue is 240 in range 0 to 360, so for opencv it would be 120
lower = (100,100,100)
upper = (160,255,255)
mask = cv2.inRange(hsv, lower, upper)

# count non-zero pixels in mask
count=np.count_nonzero(mask)
print('count:', count)

# save output
cv2.imwrite('Jamuna river data1973.png', mask)

# Display various images to see the steps
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()