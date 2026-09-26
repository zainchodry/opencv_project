import cv2
import os

image_path = "/home/enigmatix/Downloads/new_folder/Gemini_Generated_Image_uiutv2uiutv2uiut.png"

image = input("Enter the path to the image file: ")
if not os.path.isfile(image):
    print("Error: The specified file does not exist.")
else:
    image1 = cv2.imread(image)
    if image1 is not None:
        user = input("Show or Save the image? (show/save): ").strip().lower()
        if user == "show":
            gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Image", gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif user == "save":
            output_path = input("Enter the path to save the image: ")
            gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            success = cv2.imwrite(output_path, gray)
            if success:
                print(f"Image saved successfully at {output_path}.")
            else:
                print("Error: Could not save the image.")
    else:
        print("Error: Could not load the image.")