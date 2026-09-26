import cv2
import numpy as np

image = cv2.imread("/home/enigmatix/Downloads/new_folder/Gemini_Generated_Image_uiutv2uiutv2uiut.png")
if image is not None:
    cv2.imshow("Enigmatix", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")
