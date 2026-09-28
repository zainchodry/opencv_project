"""
feat: add image thresholding using OpenCV

- Apply cv2.threshold() to convert grayscale images into binary images.
- Pass the source grayscale image as the first parameter.
- Use thresh to define the pixel intensity threshold value.
- Use maxval to define the maximum output pixel value.
- Use THRESH_BINARY to convert pixels into black or white.
- Use THRESH_BINARY_INV to generate the inverse binary image.
- Use THRESH_TRUNC to limit pixels above the threshold value.
- Use THRESH_TOZERO to remove pixels below the threshold.
- Use THRESH_TOZERO_INV to remove pixels above the threshold.
- Return retval containing the threshold value used by OpenCV.
- Return the thresholded image containing the processed pixel values.
- Use the thresholded image as input for cv2.findContours().
"""

import cv2

img = image = cv2.imread("/home/enigmatix/Videos/Screencasts/oldmans.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not read image")
else:
    ret, thres_image = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
    cv2.imshow("Original Image", img)
    cv2.imshow("Thresholded Image", thres_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
