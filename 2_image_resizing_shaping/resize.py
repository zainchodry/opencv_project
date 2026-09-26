import cv2
import os
import numpy as np

image = cv2.imread("/home/enigmatix/Downloads/new_folder/Gemini_Generated_Image_uiutv2uiutv2uiut.png")
if image is None:
    print("Error:image Could not found.")
else:
    print("Image loaded successfully.")
    resized = cv2.resize(image, (300, 300))
    cv2.imshow("Resized Image", resized)
    cv2.imshow("Original Image", image)

    cv2.imwrite("resized_image.png", resized)
    print("Resized image saved successfully.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
