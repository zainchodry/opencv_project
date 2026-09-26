import cv2
import os

image = cv2.imread("/home/enigmatix/Downloads/new_folder/Gemini_Generated_Image_uiutv2uiutv2uiut.png")
if image is None:
    print("Error: Image could not be found.")
else:
    print("Image Loaded successfully.")
    (h,w) = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(image, M, (w,h))
    cv2.imshow("Rotated Image", rotated)
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    