import cv2
import numpy as np

image = cv2.imread("/home/enigmatix/Videos/Screencasts/images.jpeg")

if image is None:
    print("ERROR: Could not read image.")
else:
    kernal = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    sharpend = cv2.filter2D(image, -1, kernal)
    cv2.imshow("Original Image", image)
    cv2.imshow("Sharpened Image", sharpend)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    