#to enhance the contrast of an image using histogram equalization techniques
import cv2
import numpy as np
from matplotlib import pyplot as plt
yuvimg=cv2.cvtColor(cv2.imread('macaw.jpg'),cv2.COLOR_BGR2YUV)
yuvimg[:,:,0]=cv2.equalizeHist(yuvimg[:,:,0])
cv2.imwrite('enhanced_macaw.jpg',cv2.cvtColor(yuvimg,cv2.COLOR_YUV2BGR))
img=cv2.imread('enhanced_macaw.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('enhanced_macaw.jpg',img)
hist,bins = np.histogram(img,256,[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram for enhanced gray scale picture')
plt.show()
cv2.waitKey(10)
cv2.destroyAllWindows()