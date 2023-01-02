import cv2
import numpy as np

# reading image
img = cv2.imread("house.jpg")

# Edges
# converts image from one color space to another
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#median blur is used to smoothen the image
gray = cv2.medianBlur(gray, 5)
#transfomrs a grayscale image toa binary image
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
		cv2.THRESH_BINARY, 9, 9)

# Cartoonization
#bilatering filtering reduces noise of the image
color = cv2.bilateralFilter(img, 9, 250, 250)
#bitwise conjuction of two array
cartoon = cv2.bitwise_and(color, color, mask=edges)
#imwrite is used to save the image
cv2.imwrite("cartoon_image.jpg",cartoon)
cv2.imwrite("image_edges.jpg",edges)

# cv2.imshow("Image", img)
# cv2.imshow("edges", edges)
# cv2.imshow("Cartoon", cartoon)

# cv2.waitKey(0)
# cv2.destroyAllWindows()