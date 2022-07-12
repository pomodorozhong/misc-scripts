import cv2
img = cv2.imread("image.jpeg")

y = 1300
h = 3000
x = 500
w = 3000

crop_img = img[y:y+h, x:x+w]

# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)

filename = 'cropped-image.jpg'
cv2.imwrite(filename, crop_img)