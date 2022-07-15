import cv2
from cv2 import invert
from cv2 import blur
image1=cv2.imread('./test.jpg')
window_name1='original image'
# Displaying the original image
cv2.imshow(window_name1,image1)
# Convert the image from one color space to another
grey_img=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(grey_img)
# Image smoothing
blur=cv2.GaussianBlur(invert,(21,21),0)
invertedblur=cv2.bitwise_not(blur)
sketch=cv2.divide(grey_img,invertedblur,scale=256.0)
cv2.imwrite('./sketch.jpg',sketch)
image2=cv2.imread("./sketch.jpg")
window_name='Sketch-image'
cv2.imshow(window_name,image2)
cv2.waitKey(0)
cv2.destroyAllWindows()