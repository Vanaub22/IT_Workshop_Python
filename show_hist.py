#to show the histogram for a given greyscale image
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('macaw.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('macaw.jpg',img)
hist,bins=np.histogram(img,256,[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()