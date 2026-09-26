import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'VP80')

recorder = cv2.VideoWriter(
    '/home/enigmatix/Videos/Screencasts/output_video.webm',
    codec,
    20.0,
    (frame_width, frame_height)
)

print("Camera opened:", camera.isOpened())
print("Recorder opened:", recorder.isOpened())

while True:
    success, frame = camera.read()

    if not success:
        print("Error: Could not read frame")
        break

    recorder.write(frame)
    cv2.imshow("Recording Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

recorder.release()
camera.release()
cv2.destroyAllWindows()