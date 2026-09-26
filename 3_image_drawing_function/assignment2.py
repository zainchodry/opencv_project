import cv2
import os

image = input("Enter the path of the image: ")
if not os.path.isfile(image):
    print("Error: The specified file does not exist.")
else:
    image1 = cv2.imread(image)
    if image1 is not None:
        user = input("Do you draw a circle or text or rectangle or line on the image? (circle/text/rectangle/line): ").strip().lower()
        if user == "circle":
            p1 = int(input("Enter the x-coordinate of the center of the circle: "))
            p2 = int(input("Enter the y-coordinate of the center of the circle: "))
            radius = int(input("Enter the radius of the circle: "))
            colour = (0, 0, 256)
            thickness = 2
            cv2.circle(image1, (p1, p2), radius, colour, thickness)
            cv2.imshow("Circle Drawing", image1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif user == "text":
            text = input("Enter the text to be drawn: ")
            p1 = int(input("Enter the x-coordinate of the bottom-left corner of the text: "))
            p2 = int(input("Enter the y-coordinate of the bottom-left corner of the text: "))
            font_scale = float(input("Enter the font scale (e.g., 1.0): "))
            colour = (0, 0, 256)
            thickness = 2
            cv2.putText(image1, text, (p1, p2), cv2.FONT_HERSHEY_SIMPLEX, font_scale, colour, thickness)
            cv2.imshow("Text Drawing", image1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif user == "rectangle":
            p1_x = int(input("Enter the x-coordinate of the top-left corner of the rectangle: "))
            p1_y = int(input("Enter the y-coordinate of the top-left corner of the rectangle: "))
            p2_x = int(input("Enter the x-coordinate of the bottom-right corner of the rectangle: "))
            p2_y = int(input("Enter the y-coordinate of the bottom-right corner of the rectangle: "))
            colour = (0, 256, 0)
            thickness = 2
            cv2.rectangle(image1, (p1_x, p1_y), (p2_x, p2_y), colour, thickness)
            cv2.imshow("Rectangle Drawing", image1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif user == "line":
            p1_x = int(input("Enter the x-coordinate of the starting point of the line: "))
            p1_y = int(input("Enter the y-coordinate of the starting point of the line: "))
            p2_x = int(input("Enter the x-coordinate of the ending point of the line: "))
            p2_y = int(input("Enter the y-coordinate of the ending point of the line: "))
            colour = (256, 0, 0)
            thickness = 2
            cv2.line(image1, (p1_x, p1_y), (p2_x, p2_y), colour, thickness)
            cv2.imshow("Line Drawing", image1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Error: Invalid option. Please choose 'circle', 'text', 'rectangle', or 'line'.")