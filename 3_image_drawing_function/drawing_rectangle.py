import cv2

image = cv2.imread("/home/enigmatix/Downloads/new_folder/download.jpeg")
if image is None:
    print("Error: Image could not be found.")
else:
    p1 = (50, 50)
    p2 = (200, 200)
    colour = (0, 256, 0)
    thickness = 2
    cv2.rectangle(image, p1, p2, colour, thickness)
    cv2.imshow("Rectangle Drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    