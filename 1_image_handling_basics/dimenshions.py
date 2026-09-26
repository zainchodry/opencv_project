import cv2
import numpy as np

image = cv2.imread("/home/enigmatix/Downloads/new_folder/Gemini_Generated_Image_uiutv2uiutv2uiut.png")
if image is not None:
    h, w, c = image.shape
    print(f"Image loaded:\nHeight: {h}\nwidth: {w}\nChannels: {c}")
else:
    print("Error: Could not load the image.")
    