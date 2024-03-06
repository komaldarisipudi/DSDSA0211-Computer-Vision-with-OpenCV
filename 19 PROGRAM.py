import cv2
img = cv2.imread("C:/Users/KOMAL DARISIPUDI/Desktop/cv images/1 image.jpeg")
cv2.imshow('Original', img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)j
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) 
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)
