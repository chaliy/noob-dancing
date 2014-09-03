import numpy as np
import cv2

camera = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    (grabbed, frame) = camera.read()

    faces = cascade.detectMultiScale(frame,
      minSize = (60, 60)) # flags = CV_HAAR_SCALE_IMAGE

    for (x, y, w, h) in faces:
	     cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == 27: # ESC to exit
        break

camera.release()
cv2.destroyAllWindows()
