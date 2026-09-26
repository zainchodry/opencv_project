import cv2
import numpy as np

image = cv2.imread("/home/enigmatix/Downloads/new_folder/Gemini_Generated_Image_uiutv2uiutv2uiut.png")
if image is not None:
    success = cv2.imwrite("/home/enigmatix/Downloads/new_folder/output_python.png", image)
    if success:
        print("Image saved successfully.")
    else:
        print("Error: Could not save the image.")
else:
    print("Error: Could not load the image.")