import os
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__))
face_cascade = cv2.CascadeClassifier(dir_path + "/face_haar.xml")
img_dir_path = dir_path + "/images/"
face_dir_path = dir_path + "/faces/"
if not os.path.isdir(face_dir_path):
    os.mkdir(face_dir_path)

face_count = 0
for file in os.listdir(img_dir_path):
    filepath = img_dir_path + file
    if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        img = cv2.imread(filepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        sub_count = 0
        for (x, y, w, h) in faces:
            path = face_dir_path+str(face_count)+"_"+str(sub_count)+".jpg"
            cv2.imwrite(path, img[y:y+h, x:x+w, :])
            sub_count += 1
        face_count += 1
