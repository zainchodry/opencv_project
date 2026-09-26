import cv2

image = cv2.imread("/home/enigmatix/Downloads/new_folder/download.jpeg")
if image is None:
    print("Error: Image could not be found.")
else:
    p1 = (50, 100)
    p2 = (300, 100)
    colour = (256,0,0)
    thickness = 1
    cv2.line(image, p1, p2, colour, thickness)
    cv2.imshow("Line Drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
