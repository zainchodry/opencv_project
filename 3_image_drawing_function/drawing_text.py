import cv2

image = cv2.imread("/home/enigmatix/Downloads/new_folder/download.jpeg")
if image is None:
    print("Error: Image could not be found.")
else:
    cv2.putText(image, "Hello, OpenCV!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 256), 2)
    cv2.imshow("Text Drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()