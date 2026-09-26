import cv2
import os

image = cv2.imread("/home/enigmatix/Downloads/new_folder/Gemini_Generated_Image_uiutv2uiutv2uiut.png")
if image is not None:
    image1 = image[100:500, 100:500]
    cv2.imshow("Cropped Image", image1)
    cv2.imshow("Original Image", image)
    cv2.imwrite("cropped_image.png", image1)
    print("Cropped image saved successfully.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load the image.")
    