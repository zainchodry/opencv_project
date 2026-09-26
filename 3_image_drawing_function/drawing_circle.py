import cv2

image = cv2.imread("/home/enigmatix/Downloads/new_folder/download.jpeg")
if image is None:
    print("Error: Image could not be found.")
else:
    print("Image loaded successfully.")
    cv2.circle(image, (100, 100), 50, (0, 0, 256), 2)
    cv2.imshow("Circle Drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()