import cv2

image = cv2.imread("/home/enigmatix/Videos/Screencasts/personel_image.jpeg")

if image is None:
    print("ERROR: Could not read image.")
else:
    print("Image read successfully.")
    blurred = cv2.GaussianBlur(image, (15, 15), 0)

    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
