import cv2 

img = cv2.imread("C:/Users/ANKIT DIMRI/Pictures/Screenshots/Screenshot_20221218_025059.png")

row = img.shape[0]
column = img.shape[1]

center = (column/2, row/2)
angle = 180

r = cv2.getRotationMatrix2D(center, angle, 1)

rotate = cv2.warpAffine(img,r,(column,row))

cv2.imshow('origninal Image',img)
cv2.imshow('rotate Image',rotate)

cv2.waitKey(3000)   
cv2.destroyAllWindows() 
