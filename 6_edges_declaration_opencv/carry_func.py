import cv2

image = cv2.imread("/home/enigmatix/Videos/Screencasts/images.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not read image")
else:
    edges = cv2.Canny(image, 50, 150)
    cv2.imshow("Original Image", image)
    cv2.imshow("Edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()