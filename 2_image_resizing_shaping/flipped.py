import cv2
import os

image = cv2.imread("/home/enigmatix/Downloads/new_folder/Gemini_Generated_Image_uiutv2uiutv2uiut.png")
if image is None:
    print("Error: Image could not be found.")
else:
    horizental_image = cv2.flip(image, 1)
    vertical_image = cv2.flip(image, 0)
    both_image = cv2.flip(image, -1)
    cv2.imshow("Horizental Flipped Image", horizental_image)
    cv2.imshow("Vertical Flipped Image", vertical_image)
    cv2.imshow("Both Flipped Image", both_image)
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    