"""
feat: add contour detection using OpenCV findContours

- Apply cv2.findContours() to detect object boundaries.
- Use RETR_EXTERNAL to retrieve only the outer contours.
- Use RETR_LIST to retrieve all contours without hierarchy.
- Use RETR_CCOMP to organize contours into a two-level hierarchy.
- Use RETR_TREE to retrieve complete parent-child contour hierarchy.
- Use CHAIN_APPROX_NONE to store all contour boundary points.
- Use CHAIN_APPROX_SIMPLE to remove redundant points and save memory.
- Display and process detected contours for further image analysis.
"""

import cv2

image = cv2.imread("/home/enigmatix/Videos/Screencasts/Untitled.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(
    gray,
    200,
    255,
    cv2.THRESH_BINARY
)

contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

for contour in contours:

    approx = cv2.approxPolyDP(
        contour,
        0.01 * cv2.arcLength(contour, True),
        True
    )

    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"

    elif corners == 4:
        shape_name = "Rectangle"

    elif corners == 5:
        shape_name = "Pentagon"

    elif corners > 5:
        shape_name = "Circle"

    else:
        shape_name = "Unknown"

    cv2.drawContours(
        image,
        [approx],
        0,
        (0, 255, 0),
        3
    )

    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    cv2.putText(
        image,
        shape_name,
        (x, y),
        cv2.FONT_HERSHEY_COMPLEX,
        0.6,
        (0, 0, 256),
        1
    )


cv2.imshow("Contours", image)

cv2.waitKey(0)

cv2.destroyAllWindows()