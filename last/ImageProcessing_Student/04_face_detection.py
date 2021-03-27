import os

import cv2

dir_path = os.path.dirname(os.path.realpath(__file__))

img = cv2.imread(dir_path + '/face.jpeg')
face_cascade = cv2.CascadeClassifier(dir_path + "/face_haar.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('img', img)
cv2.waitKey()
